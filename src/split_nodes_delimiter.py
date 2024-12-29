from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    final = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            curr_string = ""
            inside_delimiter = False
            for char in node.text:
                if char == delimiter:
                    if inside_delimiter:  # Closing
                        final.append(TextNode(curr_string, text_type))
                        inside_delimiter = False
                    else:  # Opening
                        if curr_string:
                            final.append(TextNode(curr_string, TextType.TEXT))
                        inside_delimiter = True
                    curr_string = ""
                else:
                    curr_string += char

            # If we're still inside a delimiter after loop, raise an error
            if inside_delimiter:
                raise ValueError("Unmatched opening delimiter in text")

            # Appending any remaining text after loop
            if curr_string:
                final.append(TextNode(curr_string, TextType.TEXT))
        else:
            final.append(node)

    return final
