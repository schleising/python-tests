from markdown.core import markdown

MARKDOWN = """
# Heading

## Sub Heading

Some text

    import json
    data = json.loads(theString)

- Item 1
    - Sub Item 1
    - Sub Item 2
- Item 2
- Item 3
    - Sub Item 3

"""

html = markdown(MARKDOWN)

print(html)

with open('output/md_to_html.html', 'w', encoding='utf8') as outputFile:
    outputFile.write(html)
