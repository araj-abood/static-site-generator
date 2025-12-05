import unittest

from textnode import TextNode, text_node_to_html


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextNode.TextType.BOLD)
        node2 = TextNode("This is a text node", TextNode.TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_equal(self):
        node = TextNode("This is a text node", TextNode.TextType.BOLD, "i have a url")
        node1 = TextNode("This is a text node", TextNode.TextType.BOLD, "I dont have a url")
        
        self.assertNotEqual(node, node1)
        
    def test_not_equal_when_node_1_not_text_node(self):
        node = TextNode("This is a text node", TextNode.TextType.BOLD, "i have a url")
        node1 = "I  am not a text node"
        
        self.assertNotEqual(node, node1)

    def test_repr_equal(self):
        node = TextNode("This is a text node", TextNode.TextType.BOLD, "i have a url")
        
        self.assertEqual("TextNode(This is a text node, TextType.BOLD, i have a url)", repr(node))
        
class TestTextToHTMLNode(unittest.TestCase):
    
    def test_text(self):
        text_node = TextNode("Hello there",TextNode.TextType.TEXT)
        html_node = text_node_to_html(text_node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(text_node.text, html_node.value)

    def test_image(self):
        text_node = TextNode("baby.pics", TextNode.TextType.IMAGE)
        html_node = text_node_to_html(text_node)
        
        self.assertEqual(html_node.tag, "img")
        self.assertIn("src", html_node.props)
        self.assertIn("alt", html_node.props)


if __name__ == "__main__":
    unittest.main()