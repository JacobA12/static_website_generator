import unittest
from textnode import TextNode, TextType
from text_node_to_html_node import text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_node(self):
        text_node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "This is a text node")

    def test_bold_node(self):
        text_node = TextNode("This is a bold text", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<b>This is a bold text</b>")

    def test_italic_node(self):
        text_node = TextNode("This is an italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<i>This is an italic text</i>")

    def test_code_node(self):
        text_node = TextNode("This is a code text", TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<code>This is a code text</code>")

    def test_link_node(self):
        text_node = TextNode("This is a link", TextType.LINK, "https://www.example.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(
            html_node.to_html(), '<a href="https://www.example.com">This is a link</a>'
        )

    def test_image_node(self):
        text_node = TextNode(
            "This is an image", TextType.IMAGE, "https://www.example.com/image.png"
        )
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(
            html_node.to_html(),
            '<img href="https://www.example.com/image.png" alt="This is an image" />',
        )

    def test_invalid_type(self):
        text_node = TextNode("This is an invalid type", "invalid_type")
        with self.assertRaises(Exception):
            text_node_to_html_node(text_node)


if __name__ == "__main__":
    unittest.main()
