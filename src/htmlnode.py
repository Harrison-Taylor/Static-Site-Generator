class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html not implemented yet")
    
    def props_to_html(self):
        if self.props == None:
            return "" 
        final_string = ""
        for key in self.props:
            final_string += f' {key}="{self.props[key]}"'
        return final_string
    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return (
        self.tag == other.tag and
        self.value == other.value and
        self.children == other.children and
        self.props == other.props
        )


    def __repr__(self):
        return f"debugging values for an HTMLNode, this is self.tag: {self.tag}, this is self.value: {self.value}, this is self.children: {self.children}, this is self.props: {self.props}"
