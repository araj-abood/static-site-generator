import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextNode.TextType.BOLD)
        node2 = TextNode("This is a text node", TextNode.TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_equal(self):
        node = TextNode("This is a text node", TextNode.TextType.BOLD, "i have a url")
        node1 = TextNode("This is a text node", TextNode.TextType.BOLD, "I dont have a url")
        
        self.assertNotEqual(node, node1)

if __name__ == "__main__":
    unittest.main()