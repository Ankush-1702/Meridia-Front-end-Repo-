# Pasting into Product Fruits

**KB article (rich text):**
1. Open the matching file in `articles/*.html`, copy the whole contents.
2. In Product Fruits → Knowledge Base → New article, switch the editor to **Source / HTML** (the `</>` button), paste, then switch back. If the editor has no HTML mode, open the `.html` file in a browser, select all, copy, and paste into the visual editor – formatting is preserved.
3. Set the title from the first-line comment in the file.
4. Replace each orange **📷 Screenshot n** box with the real image.

**Tours / checklists:** see `tours-and-checklists.md`.

**Regenerate HTML after editing a `.md`:** `python3 ../tools/md_to_pf_html.py <article>.md articles/<article>.html`
