from textnode import TextType, TextNode
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
    def __repr__(self):
        return f"LeafNode(this is self.tag: {self.tag}, this is self.value: {self.value}, this is self.props{self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode must have a tag")
        if self.children == None:
            raise ValueError("ParentNode must have children")
        the_final_html = ""
        for child in self.children:
            the_final_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{the_final_html}</{self.tag}>" 
    
    def __repr__(self):
        return f"ParentNode(this is self.tag: {self.tag}, this is self.children: {self.children}, this is self.props{self.props})"


        
        