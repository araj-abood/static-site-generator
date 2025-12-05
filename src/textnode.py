from enum import Enum
from leafnode import LeafNode
class TextNode:
    class TextType(Enum):
        TEXT  = "text"
        BOLD   = "bold"
        ITALIC = "italic"
        CODE   = "code"
        LINK   = "link"
        IMAGE  = "image"
    
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url
        
        
    def __eq__(self, value):
        if not isinstance(value, TextNode):
            return False
        text_equal = self.text == value.text
        text_type_equal = self.text_type == value.text_type
        url_equal = self.url == value.url
        
        return text_equal and text_type_equal and url_equal
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
def text_node_to_html(text_node):
    if text_node.text_type == TextNode.TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextNode.TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextNode.TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextNode.TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextNode.TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextNode.TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise ValueError(f"invalid text type: {text_node.text_type}")