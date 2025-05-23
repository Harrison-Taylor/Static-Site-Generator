from textnode import *
from htmlnode import *
def main():
    testnode = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    test = testnode.__repr__()
    print(f"{test}")

def text_node_to_html_node(text_node):
        match text_node.text_type:
            case TextType.TEXT:
                return LeafNode(None, text_node.text, None)
            case TextType.BOLD:
                return LeafNode("b", text_node.text, None)
            case TextType.ITALIC:
                return LeafNode("i", text_node.text, None)
            case TextType.CODE:
                return LeafNode("code", text_node.text, None)
            case TextType.LINK:
                return LeafNode("a", text_node.text, {"href": text_node.url})
            case TextType.IMAGE:
                return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
            case _:
                raise Exception("invalid text type")
main()