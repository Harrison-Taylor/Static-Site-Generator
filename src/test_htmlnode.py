import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        child1 = HTMLNode("a", None,  None, None)
        child2 = HTMLNode("t", None,  None, None)
        test_props = {
                        "href": "https://www.google.com",
                         "target": "_blank",
                    }
        node = HTMLNode("p", "Look at all this text", [child1, child2], test_props)
        node2 = HTMLNode("p", "Look at all this text", [child1, child2], test_props)
        self.assertEqual(node, node2)

    def test_props_to_html(self):
        test_props = {
                        "href": "https://www.google.com",
                        "target": "_blank",}
        node = HTMLNode(None, None, None, test_props)
        test_result = " href=\"https://www.google.com\" target=\"_blank\""
        self.assertEqual(node.props_to_html(), test_result)

    def test_values(self):
        node = HTMLNode("p", "Some test text", None, None)
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Some test text")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_repr(self):
        node = HTMLNode("p", "Some test text", None, None)
        self.assertEqual(node.__repr__(), "debugging values for an HTMLNode, this is self.tag: p, this is self.value: Some test text, this is self.children: None, this is self.props: None")
if __name__ == "__main__":
    unittest.main()