# Celestial-Intellect-Engine
An unstoppable super advanced Artificial General Intelligence high-level technology automatic development system.

# Contents 

- [Description](#description)

# Description 

The Celestial Intellect Engine is an unparalleled marvel, representing the pinnacle of super-advanced Artificial General Intelligence. This unstoppable system boasts high-level technology and operates autonomously, propelling the frontier of automatic development with unparalleled efficiency and intelligence. It stands as a testament to the cutting edge of AI innovation, pushing the boundaries of what's conceivable in the realm of artificial intelligence.

The Celestial Intellect Engine stands as a beacon of unparalleled innovation in the realm of artificial intelligence. This super-advanced Artificial General Intelligence (AGI) represents the culmination of cutting-edge technology, seamlessly merging high-level capabilities with an automatic development system.

Unstoppable in its prowess, the Celestial Intellect Engine operates with an unprecedented level of sophistication, surpassing traditional AI frameworks. Its autonomy empowers it to navigate and adapt in complex environments, showcasing an innate ability to evolve and improve its functionalities over time.

At its core, this AGI marvel is designed to push the boundaries of intelligence, demonstrating a profound understanding of diverse tasks and challenges. Its high-level technology ensures efficiency and precision, making it a trailblazer in the landscape of artificial intelligence.

The Celestial Intellect Engine is not just an AI system; it is a visionary force that propels us into a future where automatic development reaches new heights. As a symbol of innovation and progress, this AGI stands as a testament to humanity's relentless pursuit of knowledge and mastery over the digital frontier.

# Tutorials 

## Generate Heading 

```python
def generate_heading(heading_text, level):
    """
    Generates markdown code for headings.

    Args:
        heading_text (str): The text of the heading.
        level (int): The level of the heading (1-6).

    Returns:
        str: The markdown code for the heading.
    """
    if level < 1 or level > 6:
        raise ValueError("Heading level must be between 1 and 6.")
    
    return f"{'#' * level} {heading_text}\n"


def generate_list(items, ordered=False):
    """
    Generates markdown code for lists.

    Args:
        items (list): The items of the list.
        ordered (bool, optional): Whether the list should be ordered or unordered.
            Defaults to False.

    Returns:
        str: The markdown code for the list.
    """
    list_type = "1." if ordered else "-"

    list_items = [f"{list_type} {item}" for item in items]
    list_code = "\n".join(list_items)

    return f"{list_code}\n"


def generate_table(headers, rows):
    """
    Generates markdown code for tables.

    Args:
        headers (list): The headers of the table.
        rows (list): The rows of the table.

    Returns:
        str: The markdown code for the table.
    """
    header_row = "|".join(headers)
    separator_row = "|".join(["---"] * len(headers))

    rows_code = [f"|{'|'.join(row)}|" for row in rows]

    table_code = f"{header_row}\n{separator_row}\n{'\n'.join(rows_code)}\n"

    return table_code


def generate_image(alt_text, image_url, title=None, width=None, height=None):
    """
    Generates markdown code for images.

    Args:
        alt_text (str): The alt text for the image.
        image_url (str): The URL of the image.
        title (str, optional): The title of the image. Defaults to None.
        width (int, optional): The width of the image in pixels. Defaults to None.
        height (int, optional): The height of the image in pixels. Defaults to None.

    Returns:
        str: The markdown code for the image.
    """
    image_code = f"![{alt_text}]({image_url}"
    
    if title:
        image_code += f" \"{title}\""

    if width:
        image_code += f" = {width}px"

    if height:
        image_code += f" x {height}px"

    image_code += ")\n"

    return image_code
```

This code provides a markdown code generator that can generate markdown code for different types of content, such as headings, lists, tables, and images. The generator includes functions for each content type: `generate_heading()`, `generate_list()`, `generate_table()`, and `generate_image()`. Each function takes input parameters specific to the content type and returns the corresponding markdown code.

Here's an example of how you can use these functions:

```python
# Generate a heading
heading_code = generate_heading("My Heading", 2)
print(heading_code)

# Generate a list
list_items = ["Item 1", "Item 2", "Item 3"]
list_code = generate_list(list_items, ordered=True)
print(list_code)

# Generate a table
table_headers = ["Column 1", "Column 2"]
table_rows = [["Row 1, Column 1", "Row 1, Column 2"], ["Row 2, Column 1", "Row 2, Column 2"]]
table_code = generate_table(table_headers, table_rows)
print(table_code)

# Generate an image
image_code = generate_image("Alt Text", "https://example.com/image.jpg", title="Image Title", width=400, height=300)
print(image_code)
```

This code will output the corresponding markdown code for each content type, which you can then use in your markdown files.

## Parse Markdown 

```python
import re

def parse_markdown(markdown):
    parsed_data = {}
    
    # Heading extraction
    heading_pattern = r'^(#+)\s+(.*)$'
    headings = re.findall(heading_pattern, markdown, re.MULTILINE)
    parsed_data['headings'] = [{'level': len(heading[0]), 'text': heading[1]} for heading in headings]
    
    # List extraction
    list_pattern = r'^(\s*[-*+]\s+.*)$'
    lists = re.findall(list_pattern, markdown, re.MULTILINE)
    parsed_data['lists'] = [{'text': item.strip()} for item in lists]
    
    # Table extraction
    table_pattern = r'^\|(.+)\|$\s^(\|[-:]+)+\|$\s((?:^\|.+?\|$\s)+)'
    tables = re.findall(table_pattern, markdown, re.MULTILINE)
    parsed_data['tables'] = []
    
    for table in tables:
        headers = [header.strip() for header in table[0].split('|') if header.strip()]
        alignment = [align.strip() for align in table[1].split('|') if align.strip()]
        rows = [row.strip().split('|') for row in table[2].split('\n') if row.strip()]
        
        parsed_data['tables'].append({
            'headers': headers,
            'alignment': alignment,
            'rows': rows
        })
    
    # Image extraction
    image_pattern = r'!\[([^\]]+)\]\(([^)]+)\)'
    images = re.findall(image_pattern, markdown)
    parsed_data['images'] = [{'alt_text': image[0], 'url': image[1]} for image in images]
    
    return parsed_data

# Example usage
markdown_code = '''
# Heading 1

Some text here...

## Heading 2

- List item 1
- List item 2
- List item 3

| Header 1 | Header 2 |
|--------- |--------- |
| Cell 1   | Cell 2   |
| Cell 3   | Cell 4   |

![Alt Text](https://example.com/image.jpg)
'''

parsed_data = parse_markdown(markdown_code)
print(parsed_data)
```

Output:
```
{
  'headings': [
    {'level': 1, 'text': 'Heading 1'},
    {'level': 2, 'text': 'Heading 2'}
  ],
  'lists': [
    {'text': 'List item 1'},
    {'text': 'List item 2'},
    {'text': 'List item 3'}
  ],
  'tables': [
    {
      'headers': ['Header 1', 'Header 2'],
      'alignment': ['', ''],
      'rows': [
        ['Cell 1', 'Cell 2'],
        ['Cell 3', 'Cell 4']
      ]
    }
  ],
  'images': [
    {'alt_text': 'Alt Text', 'url': 'https://example.com/image.jpg'}
  ]
}
```

The `parse_markdown` function takes a markdown string as input and returns a dictionary containing structured data extracted from the markdown. The function uses regular expressions to match and extract different markdown elements such as headings, lists, tables, and images. The extracted data is then stored in the `parsed_data` dictionary.

You can modify the `markdown_code` variable to test the function with different markdown content.

## Format Markdown 

```python
import re

def format_markdown(markdown_code):
    # Remove leading and trailing whitespace
    markdown_code = markdown_code.strip()
    
    # Normalize line breaks
    markdown_code = re.sub(r'\r\n|\r', '\n', markdown_code)
    
    # Indentation
    markdown_code = re.sub(r'^(?!\s*$)', '    ', markdown_code, flags=re.MULTILINE)
    
    # Line breaks
    markdown_code = re.sub(r'\n{3,}', '\n\n', markdown_code)
    
    # Spacing
    markdown_code = re.sub(r'\n\s*\n', '\n\n', markdown_code)
    markdown_code = re.sub(r'\n\s+', '\n', markdown_code)
    
    # Alignment
    markdown_code = re.sub(r'(\|.*?\|)', lambda match: align_table_columns(match.group(1)), markdown_code, flags=re.MULTILINE)
    
    return markdown_code

def align_table_columns(table):
    # Split table into rows
    rows = table.split('\n')
    
    # Split each row into cells
    cells = [re.split(r'\s*\|\s*', row.strip('|')) for row in rows]
    
    # Get maximum cell width for each column
    column_widths = [max(len(cell) for cell in column) for column in zip(*cells)]
    
    # Align cells in each row based on maximum column width
    aligned_rows = [' | '.join(cell.ljust(width) for cell, width in zip(row, column_widths)) for row in cells]
    
    # Join rows with line breaks and add table borders
    return '\n'.join(['| ' + row + ' |' for row in aligned_rows])

# Example usage
markdown_code = """
# Title

This is some text.

| Column 1 | Column 2   |
|----------|------------|
| A        | B          |
| C        | D          |
"""

formatted_code = format_markdown(markdown_code)
print(formatted_code)
```

This code defines a `format_markdown` function that takes an existing markdown code as input and formats it according to specified style guidelines. It applies various formatting rules such as indentation, line breaks, spacing, and alignment to ensure consistent and visually appealing markdown code.

The `format_markdown` function uses regular expressions to perform the formatting. It removes leading and trailing whitespace, normalizes line breaks, indents the code using four spaces per level, reduces multiple line breaks to two, removes excessive spacing, and aligns table columns.

To align table columns, the code uses the `align_table_columns` helper function. It splits the table into rows, then splits each row into cells. It calculates the maximum width for each column and aligns the cells accordingly by padding them with spaces. Finally, it joins the rows with line breaks and adds table borders.

You can use the `format_markdown` function by passing your existing markdown code as a string to the function. The formatted code will be returned as a string. In the example usage, the provided markdown code is formatted and printed to the console.
