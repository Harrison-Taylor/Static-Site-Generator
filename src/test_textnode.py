import unittest
from main import text_node_to_html_node
from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_image(self):
        node = TextNode("Some image description", TextType.IMAGE, "www.bootdev.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props_to_html(), " src=\"www.bootdev.com\" alt=\"Some image description\"")

    def test_link(self):
        node = TextNode("Some anchor text", TextType.LINK, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Some anchor text")
        self.assertEqual(html_node.props_to_html(), " href=\"https://www.google.com\"")

    def test_bold(self):
        node = TextNode("Some bold text", TextType.BOLD, None)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Some bold text")

if __name__ == "__main__":
    unittest.main()