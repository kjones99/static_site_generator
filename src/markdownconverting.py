from blockhandling import block_to_block_type, markdown_to_blocks, BlockType
from parentnode import ParentNode
from splitfuncs import text_to_textnodes
from textnode import TextNode, text_node_to_html_node, TextType

#take a whole markdown file and return a single parent HTML node
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_list = []
    for block in blocks:
        block_type = block_to_block_type(block)
        #if the block is a heading we need to count the number of hashes to determine the appropriate number to put in the heading
        if block_type == BlockType.HEADING:
            tag = f'h{len(block.split(' ')[0])}'
        #if the block isn't a heading we can just pull the tag from the BlockType enum
        else:
            tag = block_type.value
        #create a parent node for the block and use a call to text_to_children to populate the list of children HTML nodes
        block_node = ParentNode(tag, text_to_children(block, block_type))
        block_list.append(block_node)
    #create a div parent node for the whole file and use the list of Block HTML nodes as the children variable
    return ParentNode('div', block_list)

#based on the block type prepare the block by stripping markdown indicators then create HTML child nodes
def text_to_children(text_block, block_type):
    child_nodes = []
    #call the text to html nodes function, no parsing of the block necessary
    if block_type == BlockType.PARAGRAPH:
        text_block = text_block.replace('\n', ' ')
        child_nodes = text_to_html_nodes(text_block.lstrip())

    #remove all the '#' chars from the start of the block
    elif block_type == BlockType.HEADING:
        heading_num = len(text_block.split(' ')[0])
        child_nodes = text_to_html_nodes(text_block[heading_num+1:].lstrip())

    #parse the block to remove '>' from the start of every line
    elif block_type == BlockType.QUOTE:
        text_block_lines = text_block.split('\n')
        text_block_lines = [line[1:] for line in text_block_lines]
        text_block = '\n'.join(text_block_lines)  
        child_nodes = text_to_html_nodes(text_block.lstrip())

    #create a child_nodes list containing a 'pre' ParentNode, this parent node will in turn have a child node 
    #containing the whole text block with no splitting
    elif block_type == BlockType.CODE:
        child_nodes = [ParentNode('code', [text_node_to_html_node(TextNode(text_block[3:-3].lstrip(), TextType.TEXT))])]

    #split block into lines and wrap all of the HTML nodes for each line with a parent 'li' node
    elif block_type == BlockType.ORDERED_LIST:
        text_lines = text_block.split('\n')
        for line in text_lines:
            child_nodes.append(ParentNode('li', text_to_html_nodes(line[3:])))
    
    #same as the ordered list but only have to strip the first 2 chars from each line instead of 3
    elif block_type == BlockType.UNORDERED_LIST:
        text_lines = text_block.split('\n')
        for line in text_lines:
            child_nodes.append(ParentNode('li', text_to_html_nodes(line[2:])))

    return child_nodes

#parse the text and create a list of text nodes then convert them to HTML nodes
def text_to_html_nodes(text_block):
    text_nodes = text_to_textnodes(text_block)
    child_nodes = [text_node_to_html_node(node) for node in text_nodes]
    return child_nodes

def extract_title(markdown):
    for line in markdown.split('\n'):
        if line[0:2] == '# ':
            return line[2:].strip()
    raise Exception("No h1 header found in the markdown file")