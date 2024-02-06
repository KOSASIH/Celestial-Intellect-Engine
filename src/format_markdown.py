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
