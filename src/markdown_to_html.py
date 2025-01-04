from markdown_blocks import (
    markdown_to_blocks,
    block_to_block_type,
    block_to_text_content,
)
from htmlnode import HTMLNode, ParentNode, LeafNode
from inline_markdown import *


def markdown_to_html_node(markdown):
    filtered_blocks = markdown_to_blocks(markdown)
    types = []
    master_parent = ParentNode("div")

    for block in filtered_blocks:
        curr_type = block_to_block_type(block)
        types.append(curr_type)
        new_node = None

        if curr_type == "heading":
            heading_num = get_heading_num(block)
            new_node = ParentNode(f"h{heading_num}")
            new_node.add_child(text_to_children(block_to_text_content(block)))
        if curr_type == "paragraph":
            new_node = ParentNode("p")
            new_node.add_child(text_to_children(block_to_text_content(block)))
        if curr_type == "code":
            code_node = ParentNode("code", children=text_to_children(block))
            new_node = ParentNode("pre", [code_node])
        if curr_type == "quote":
            new_node = ParentNode("quote")
            new_node.add_child(text_to_children(block_to_text_content(block)))
        if curr_type == "ordered_list":
            new_node = ParentNode("ol")
            new_node.add_child(text_to_children(block_to_text_content(block)))
        if curr_type == "unordered_list":
            new_node = ParentNode("ul")
            new_node.add_child(text_to_children(block_to_text_content(block)))

        master_parent.add_child(new_node)

    return master_parent


def text_to_children(block):
    nodes = text_to_textnodes(block)
    html_nodes = []

    for node in nodes:
        if node.text_type == TextType.BOLD:
            html_nodes.append(ParentNode("strong", children=[TextNode(node.text)]))
        elif node.text_type == TextType.ITALIC:
            html_nodes.append(HTMLNode("em", children=[TextNode(node.text)]))
        elif node.text_type == TextType.CODE:
            html_nodes.append(HTMLNode("code", children=[TextNode(node.text)]))
        elif node.text_type == TextType.IMAGE:
            html_nodes.append(HTMLNode("img", src=node.additional, alt=node.text))
        elif node.text_type == TextType.LINK:
            html_nodes.append(
                HTMLNode("a", href=node.additional, children=[TextNode(node.text)])
            )
        else:
            html_nodes.append(TextNode(node.text))
    return html_nodes


def get_heading_num(block):
    heading_num = 0
    for char in block:
        if char == "#":
            heading_num += 1
        else:
            break
    return heading_num
