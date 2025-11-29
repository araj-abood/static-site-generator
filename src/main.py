from textnode import TextNode

def main():
    text_node = TextNode("Hello world", TextNode.TextType.CODE, "Hello")
    
    print(text_node)
    return 0
    
main()