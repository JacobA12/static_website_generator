import unittest
from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter, split_nodes_link, split_nodes_images


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_single_node(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_multiple_nodes(self):
        nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("`code`", TextType.TEXT),
            TextNode(" and ", TextType.TEXT),
            TextNode("`more code`", TextType.TEXT),
        ]
        new_nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" and ", TextType.TEXT),
            TextNode("more code", TextType.CODE),
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_no_delimiter(self):
        node = TextNode("This is text without code blocks", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [TextNode("This is text without code blocks", TextType.TEXT)]
        self.assertEqual(new_nodes, expected)

    def test_split_empty_nodes(self):
        nodes = []
        new_nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
        expected = []
        self.assertEqual(new_nodes, expected)

    def test_split_unmatched_delimiter(self):
        node = TextNode("This is text with an `unmatched code block", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_split_nodes_link(self):
        node = TextNode("This is a [link](https://www.example.com)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://www.example.com"),
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_nodes_images(self):
        node = TextNode("This is an ![image](https://www.example.com/image.png)", TextType.TEXT)
        new_nodes = split_nodes_images([node])
        expected = [
            TextNode("This is an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://www.example.com/image.png"),
        ]
        self.assertEqual(new_nodes, expected)


if __name__ == "__main__":
    unittest.main()
