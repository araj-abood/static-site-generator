from textnode import TextNode
from extract_markdown import extract_markdown_image, extrack_mark_down_link


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextNode.TextType.TEXT:
            new_nodes.append(node)
            continue
        
        split_nodes = []
        sections = node.text.split(delimiter)

        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown")
        
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextNode.TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
                
        new_nodes.extend(split_nodes)
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextNode.TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_image(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextNode.TextType.TEXT))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextNode.TextType.IMAGE,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextNode.TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextNode.TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extrack_mark_down_link(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextNode.TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextNode.TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextNode.TextType.TEXT))
    return new_nodes


def text_to_textnodes(text):
    nodes = [TextNode(text, TextNode.TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextNode.TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextNode.TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextNode.TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes


    