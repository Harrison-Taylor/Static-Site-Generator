from enum import Enum

TextType = Enum("TextType", ["NORMAL", "BOLD", "ITALIC", "CODE", "LINK", "IMAGE"])

class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other_text_node):
        if self.text == other_text_node.text & self.text_type == other_text_node.text_type & self.url == other_text_node.url:
            return True
        return False

    def __repr__(self):
        start = "TextNode("
        first = self.text +", "
        second = self.text_type.name +", "
        last = self.url + ")"
        final_string = start + first + second + last
        return final_string
