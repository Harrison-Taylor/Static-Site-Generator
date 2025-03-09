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

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            return ValueError("Leafnode must have a value")      
        if self.tag == None:
            return self.value
        html_props = self.props_to_html()
        front_tag = f"<{self.tag}{html_props}>" 
        back_tag = f"</{self.tag}>"
        
        return front_tag + self.value + back_tag

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode must have a tag")
        if self.children == None:
            raise ValueError("ParentNode must have children")
        parent_front = f"<{self.tag}>"
        parent_back = f"</{self.tag}>"
        the_final_html = ""
        if len(self.children) == 0:
            return the_final_html
        first_node = self.children[0]
        if first_node is isinstance(ParentNode):
            parent_front += f"<{first_node.tag}>"
            parent_back = f"</{first_node.tag}>" + parent_back
        elif first_node is isinstance(LeafNode):
            first_node.to_html()
        else:
            raise TypeError("Child must be either a ParentNode or a LeafNode")


        
        