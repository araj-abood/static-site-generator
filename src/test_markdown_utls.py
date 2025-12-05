import unittest
from markdown_utils import (
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link
)

from textnode import TextNode


class TestMarkDownUtils(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextNode.TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextNode.TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextNode.TextType.TEXT),
                TextNode("bolded", TextNode.TextType.BOLD),
                TextNode(" word", TextNode.TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextNode.TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextNode.TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextNode.TextType.TEXT),
                TextNode("bolded", TextNode.TextType.BOLD),
                TextNode(" word and ", TextNode.TextType.TEXT),
                TextNode("another", TextNode.TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextNode.TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextNode.TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextNode.TextType.TEXT),
                TextNode("bolded word", TextNode.TextType.BOLD),
                TextNode(" and ", TextNode.TextType.TEXT),
                TextNode("another", TextNode.TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an _italic_ word", TextNode.TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextNode.TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextNode.TextType.TEXT),
                TextNode("italic", TextNode.TextType.ITALIC),
                TextNode(" word", TextNode.TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextNode.TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextNode.TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextNode.TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextNode.TextType.BOLD),
                TextNode(" and ", TextNode.TextType.TEXT),
                TextNode("italic", TextNode.TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextNode.TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextNode.TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextNode.TextType.TEXT),
                TextNode("code block", TextNode.TextType.CODE),
                TextNode(" word", TextNode.TextType.TEXT),
            ],
            new_nodes,
        )
        
    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextNode.TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextNode.TextType.TEXT),
                TextNode("image", TextNode.TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.COM/IMAGE.PNG)",
            TextNode.TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextNode.TextType.IMAGE, "https://www.example.COM/IMAGE.PNG"),
            ],
            new_nodes,
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextNode.TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextNode.TextType.TEXT),
                TextNode("image", TextNode.TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextNode.TextType.TEXT),
                TextNode(
                    "second image", TextNode.TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            TextNode.TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextNode.TextType.TEXT),
                TextNode("link", TextNode.TextType.LINK, "https://boot.dev"),
                TextNode(" and ", TextNode.TextType.TEXT),
                TextNode("another link", TextNode.TextType.LINK, "https://blog.boot.dev"),
                TextNode(" with text that follows", TextNode.TextType.TEXT),
            ],
            new_nodes,
        )
        
    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextNode.TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextNode.TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextNode.TextType.ITALIC)
        self.assertEqual(
            [
                TextNode("bold", TextNode.TextType.BOLD),
                TextNode(" and ", TextNode.TextType.TEXT),
                TextNode("italic", TextNode.TextType.ITALIC),
            ],
            new_nodes,
        )



if __name__ == "__main__":
    unittest.main()
