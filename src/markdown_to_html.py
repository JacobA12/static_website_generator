from markdown_blocks import markdown_to_blocks, block_to_block_type
from htmlnode import HTMLNode

def markdown_to_html_blocks(markdown):
  #Step 1: split the markdown into blocks
  filtered_blocks = markdown_to_blocks(markdown)
  
  #Step 2: For Each Block
  #Determine the block type 
  for block in filtered_blocks:
    type = block_to_block_type(block)
    #Create an HTML Node for that block type
    new_htmlNode = HTMLNode(type, block)
    