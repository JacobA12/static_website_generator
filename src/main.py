from textnode import TextNode, TextType
from static_to_public import static_to_public
import os


def main():
    current_directory = "static"
    destination = "public"
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)

    static_to_public(current_directory, destination)


main()
