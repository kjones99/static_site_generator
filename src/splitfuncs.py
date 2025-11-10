import re
from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text_sections = node.text.split(delimiter)
        if len(text_sections) % 2 == 0:
            raise Exception("Error: unmatched delimiter")
        for i in range(len(text_sections)):
            if text_sections[i] == "":
                continue
            elif i % 2 == 0:
                new_nodes.append(TextNode(text_sections[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(text_sections[i], text_type))
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        image_strs = extract_markdown_images(node.text)
        if len(image_strs) == 0:
            new_nodes.append(node)
            continue
        for image_tup in image_strs:
            pre_image_str = node.text.split('![')[0]
            if pre_image_str != "":
                new_nodes.append(TextNode(pre_image_str, TextType.TEXT))
            node.text = node.text.replace(f'{pre_image_str}![{image_tup[0]}]({image_tup[1]})', "")
            new_nodes.append(TextNode(image_tup[0], TextType.IMAGE, image_tup[1]))
        if node.text:
            new_nodes.append(TextNode(node.text, TextType.TEXT))
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        link_strs = extract_markdown_links(node.text)
        if len(link_strs) == 0:
            new_nodes.append(node)
            continue
        for link_tup in link_strs:
            pre_link_str = node.text.split(f'[{link_tup[0]}')[0]
            if pre_link_str != "":
                new_nodes.append(TextNode(pre_link_str, TextType.TEXT))
            node.text = node.text.replace(f'{pre_link_str}[{link_tup[0]}]({link_tup[1]})', "")
            new_nodes.append(TextNode(link_tup[0], TextType.LINK, link_tup[1]))
        if node.text:
            new_nodes.append(TextNode(node.text, TextType.TEXT)) 
    return new_nodes

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)",text)
    return matches

def text_to_textnodes(text):
    new_nodes = [TextNode(text, TextType.TEXT)]
    new_nodes = split_nodes_delimiter(new_nodes, '**', TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, '_', TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, '`', TextType.CODE)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    return new_nodes