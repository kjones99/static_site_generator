from enum import Enum

class BlockType(Enum):
    PARAGRAPH = 'p'
    HEADING = 'h'
    CODE = 'pre'
    QUOTE = 'blockquote'
    UNORDERED_LIST = 'ul'
    ORDERED_LIST = 'ol'

def markdown_to_blocks(markdown):
    #split block into multiple strings by splitting over empty lines
    blocks = markdown.split('\n\n')
    #strip leading and trailing whitespace from each string
    blocks = [s.strip() for s in blocks]
    #remove any empty strings from the list
    blocks = [s for s in blocks if s]
    return blocks

def block_to_block_type(block):
    #create a list of block lines
    block_lines = block.split('\n')
    #pull the leading characters to check against for certain block types
    start_chars = block.split(' ')[0]

    #check block type indicator characters
    if start_chars == '#' * len(start_chars) and block[len(start_chars)] == ' ' and len(start_chars) < 7:
        return BlockType.HEADING
    elif block[0:3] == '```' and block[-3:] == '```':
        return BlockType.CODE
    elif all(s[0] == '>' for s in block_lines):
        return BlockType.QUOTE
    elif all(s[0:2] == '- ' for s in block_lines):
        return BlockType.UNORDERED_LIST
    elif all(s[0:3] == f'{block_lines.index(s) + 1}. ' for s in block_lines):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
    