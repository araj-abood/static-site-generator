import unittest
from leafnode import LeafNode
class TestLeafNode(unittest.TestCase):
    def test__leaf_to_html_p(self):
        node = LeafNode("p", "Hello there friends", None)
        
        self.assertEqual(node.to_html(), "<p>Hello there friends</p>")
        
        
if __name__ == "main":
    unittest.main()