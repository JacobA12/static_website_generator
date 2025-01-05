from htmlnode import *
from markdown_blocks import *


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line.lstrip("#").strip()
    raise Exception("No Title Found")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        markdown = f.read()
    html = markdown_to_html_node(markdown).to_html()
