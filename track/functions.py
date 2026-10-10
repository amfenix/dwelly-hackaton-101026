"""The track's functions: lookups and actions against the world (world.json).

A function gets a `ctx` and returns the fields it found, as a dict. It never decides: the policy
reads what it returns. It records anything it does in the world with `ctx.act(...)`.

    ctx.case      the case as it came in            ctx.world   the records (world.json)
    ctx.fields    the facts known so far (read only) ctx.args    the agent's arguments, for a signal's rule
    ctx.key       the same on every retry: dedupe writes on it
    ctx.act(type, **args)       record an action taken in the world
    ctx.classify(text, {...})   ctx.generate(system, prompt)   when a check needs a model
"""

from __future__ import annotations

import threading
from typing import Any

from desk import Context, function

_PAID: set[str] = set()
"""Payments already made, by idempotency key: a retry after a lost answer does not pay twice.

It stands in for the payment API's own idempotency: a real integration sends `ctx.key` as the
request's idempotency key and lets that system dedupe, so it holds across restarts and workers.
"""
_PAYING = threading.Lock()


def _customer_of(world: dict[str, Any], sender: Any) -> tuple[str, dict[str, Any]] | None:
    for customer_id, customer in world["customers"].items():
        if customer["email"] == sender:
            return customer_id, customer
    return None


@function
def find_customer(ctx: Context) -> dict[str, Any]:
    """Who sent it, their limit, and the request's amount and payee when the payee is theirs."""
    found = _customer_of(ctx.world, ctx.case.get("from"))
    if found is None:
        ctx.note("the sender is not a customer on record")
        return {}
    customer_id, customer = found
    facts: dict[str, Any] = {"customer": customer_id, "limit": customer["limit"]}
    request = ctx.case.get("request") or {}
    if "amount" in request:
        facts["amount"] = request["amount"]
    if request.get("payee") in customer["payees"]:
        facts["payee"] = request["payee"]
    elif "payee" in request:
        ctx.note(f"payee {request['payee']} is not one of the customer's payees")
    return facts


@function
def make_payment(ctx: Context) -> dict[str, Any]:
    with _PAYING:
        if ctx.key not in _PAID:
            amount, payee = ctx.fields["amount"], ctx.fields["payee"]
            ctx.act("payment", customer=ctx.fields["customer"], payee=payee, amount=str(amount), key=ctx.key)
            _PAID.add(ctx.key)
    return {"paid": True}


@function
def brief(ctx: Any) -> str:
    """What the agent reads first: the message, and the records that matter to it."""
    facts = {k: str(v) for k, v in ctx.fields.items() if v is not None}
    return "\n".join(
        [
            "A message to the payments inbox:",
            "<case>",
            str(ctx.case.get("text", "")),
            "</case>",
            f"From: {ctx.case.get('from')}",
            f"What the desk has established: {facts or 'nothing yet'}",
            f"Case state: {ctx.state}",
        ]
    )
