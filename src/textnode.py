from enum import Enum

class TextNode:
    class TextType(Enum):
        PLAIN  = "plain"
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