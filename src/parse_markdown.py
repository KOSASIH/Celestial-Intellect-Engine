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
