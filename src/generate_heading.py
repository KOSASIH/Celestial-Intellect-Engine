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
