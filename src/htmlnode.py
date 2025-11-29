class HTMLNode:
    
    def __init__(self, tag= None, value= None, children= None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        output = ""
        
        
        if self.props is None:
            return output
        
        for key in self.props:
            output += f" {key}=\"{self.props[key]}\""
        return output
            
            
    def __repr__(self):
        return f"HtmlNode({self.tag}, {self.value}, {self.children}, {self.props})"