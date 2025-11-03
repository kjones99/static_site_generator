from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("invalid HTML: no tag")
        elif not self.children:
                raise ValueError("invalid list of leaf nodes")
        children_str = f'<{self.tag}{self.props_to_html()}>'
        for child in self.children:
             children_str += child.to_html()
        return f'{children_str}</{self.tag}>'
        
        