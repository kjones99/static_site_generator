
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        node_str = ''
        if self.tag:
            node_str += f'tag: {self.tag}\n'
        if self.value:
            node_str += f'text: {self.value}\n'
        if self.props:
            node_str += f'{self.props_to_html()}\n'
        if self.children:
            node_str += 'Child HTML Nodes'
            for i in range(len(self.children)):
                node_str += f'\n{self.children[i].__repr__()}'
        return node_str
    
#create base version of to_html to be overwritten by child classes
    def to_html(self):
        raise NotImplementedError
    
#modify props field to proper HTML format if the node has a value stored
    def props_to_html(self):
        props_str = ''
        if not self.props:
            return props_str
        for key in self.props:
            props_str += f' {str(key)}="{str(self.props[key])}"'
        return props_str