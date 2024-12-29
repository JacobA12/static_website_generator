import re

from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def split_nodes_images(old_nodes):
    final = []
    for node in old_nodes:
        # Extract markdown images from the text
        extracted_image_nodes = extract_markdown_images(node.text)

        last_index = 0  # Track where the last split leaves off
        for image_alt, image_link in extracted_image_nodes:
            # Split the text on the current image markdown
            sections = node.text.split(f"![{image_alt}]({image_link})", 1)
            # Create and append TextNode for the text before the image, if it exists
            if sections[0]:
                final.append(TextNode(sections[0], TextType.TEXT))
            # Create and append the TextNode for the image
            final.append(TextNode(f"![{image_alt}]({image_link})", TextType.IMAGE))

            # Update the node text to sections[1] to remove processed part
            node.text = sections[1]

        # Append any remaining text in node
        if node.text:
            final.append(TextNode(node.text, TextType.TEXT))

    return final


def split_nodes_link(old_nodes):
    final = []
    for node in old_nodes:
        extracted_link_nodes = extract_markdown_links(node.text)

        for link_alt, url in extracted_link_nodes:
            sections = node.text.split(f"[{link_alt}]({url})", 1)
            if sections[0]:
                final.append(TextNode(sections[0], TextType.TEXT))

            # Create the TextNode for the link with the correct representation
            final.append(TextNode(link_alt, TextType.LINK, url))

            node.text = sections[1]

        if node.text:
            final.append(TextNode(node.text, TextType.TEXT))

    return final
