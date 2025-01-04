class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value
        if self.tag is "img":
            return f"<{self.tag}{self.props_to_html()} />{self.value}"

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, props)
        self.children = children

    def to_html(self):
        if self.tag == None:
            raise ValueError("This ParentNode has no tag")
        if self.children == None:
            raise ValueError("This ParentNode has no children")

        childHtml = []
        for node in self.children:
            childHtml.append(node.to_html())
        final = f"<{self.tag}>"
        for child in childHtml:
            final += child
        final += f"</{self.tag}>"
        return final

    def add_child(self, child):
        self.children.append(child)
