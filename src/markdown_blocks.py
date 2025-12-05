def markdown_to_blocks(markdown):
    filtered_blocks = []
    
    lines = markdown.split("\n\n")
    
    for line in lines:
        
        if line == "":
            continue
        line = line.split()
        filtered_blocks.append(line)
        
    return filtered_blocks