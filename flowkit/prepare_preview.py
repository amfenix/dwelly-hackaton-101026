"""Make the Flowkit HTML export navigable and responsive in a regular browser.

Run after exporting the report screens into flowkit/preview.
"""

from pathlib import Path
import re

root = Path(__file__).resolve().parent
screens = root / "preview" / "screens"
names = ("results", "handoffs", "case-review", "policy-explorer")
for page in screens.glob("*.html"):
    viewport = "mobile" if "@mobile" in page.name else "desktop"
    html = page.read_text()
    html = re.sub(r'content="width=\d+, initial-scale=1"',
                  'content="width=device-width, initial-scale=1"', html)
    for name in names:
        html = html.replace(f'href="#{name}"', f'href="{name}@{viewport}.html"')
    page.write_text(html)

print(f"Prepared {len(list(screens.glob('*.html')))} responsive preview pages.")
