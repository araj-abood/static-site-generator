import unittest
from extract_markdown import extrack_mark_down_link, extract_markdown_image




class TestExtractMMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_image(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        
    def test_extrack_markdown_links(self):
        matches = extrack_mark_down_link(
            "This is text with a link [to boot dev](https://www.boot.dev)"
        )

        self.assertEqual([("to boot dev", "https://www.boot.dev")], matches)
