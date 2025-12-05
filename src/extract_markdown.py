import re
def extract_markdown_image(text):
    
    results = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return results

def extrack_mark_down_link(text):
    
    results = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return results
