import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("p", "", "", {"href": "google.com", "target": "_blank"})
        
        self.assertEqual(node.props_to_html(), ' href="google.com" target="_blank"')
    def test_values(self):
        node = HTMLNode("div", 
                        "what the helly", 
                        None, 
                        None
        )
        
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "what the helly")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)
        
        
        
if __name__ == "__main__":
    unittest.main()