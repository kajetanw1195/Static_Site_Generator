from htmlnode import *

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props)

    def to_html(self):
        if self.value == 0:
            raise ValueError
        if not self.tag:
            return self.value
        if self.props != None:
            x = HTMLNode.props_to_html(self.props)
            return f"<{self.tag} {x}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"