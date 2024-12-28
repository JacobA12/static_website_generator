from textnode import TextNode, TextType
from htmlnode import HTMLNode, ParentNode, LeafNode


def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(tag=None, value=f"{text_node.text}")
    elif text_node.text_type == TextType.BOLD:
        return LeafNode(tag="b", value=f"{text_node.text}")
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode(tag="i", value=f"{text_node.text}")
    elif text_node.text_type == TextType.CODE:
        return LeafNode(tag="code", value=f"{text_node.text}")
    elif text_node.text_type == TextType.LINK:
        return LeafNode(
            tag="a", value=f"{text_node.text}", props={"href": text_node.url}
        )
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode(
            tag="img", value="", props={"href": text_node.url, "alt": text_node.text}
        )
    else:
        raise Exception("Not a valid type")
