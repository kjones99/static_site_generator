import unittest
from blockhandling import markdown_to_blocks, block_to_block_type, BlockType


class TestLeafNode(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_excessive_new_lines(self):
        md = """
This is **bolded** paragraph



This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line





- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_single_block(self):
        md = """




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line






"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            ],
        )



    def test_block_heading(self):
        md = "###### Heyo"
        blocks = block_to_block_type(md)
        self.assertEqual(
            blocks,
            BlockType.HEADING
        )
    
    def test_block_heading_too_many_hashes(self):
        md = "####### Heyo"
        blocks = block_to_block_type(md)
        self.assertEqual(
            blocks,
            BlockType.PARAGRAPH
        )

    def test_block_heading_no_space_after_hashes(self):
        md = "###Heyo"
        blocks = block_to_block_type(md)
        self.assertEqual(
            blocks,
            BlockType.PARAGRAPH
        )

    def test_block_code(self):
        md = "```####### Heyo```"
        blocks = block_to_block_type(md)
        self.assertEqual(
            blocks,
            BlockType.CODE
        )

    def test_block_code_not_enough_ticks(self):
        md = "```####### Heyo``"
        blocks = block_to_block_type(md)
        self.assertEqual(
            blocks,
            BlockType.PARAGRAPH
        )

    def test_block_quote(self):
        md = """>This is the first line
>This is the second one
>This is the third"""
        blocks = block_to_block_type(md)
        self.assertEqual(
            blocks,
            BlockType.QUOTE
        )

    def test_block_quote_missing_arrow(self):
        md = """>This is the first line
This is the second one
>This is the third"""
        blocks = block_to_block_type(md)
        self.assertEqual(
            blocks,
            BlockType.PARAGRAPH
        )

    def test_block_unordered_list(self):
        md = """- This is the first line
- This is the second one
- This is the third"""
        blocks = block_to_block_type(md)
        self.assertEqual(
            blocks,
            BlockType.UNORDERED_LIST
        )

    def test_block_ordered_list(self):
        md = """1. This is the first line
2. This is the second one
3. This is the third"""
        blocks = block_to_block_type(md)
        self.assertEqual(
            blocks,
            BlockType.ORDERED_LIST
        )

    def test_block_ordered_list_incorrect_numbers(self):
        md = """2. This is the first line
2. This is the second one
3. This is the third"""
        blocks = block_to_block_type(md)
        self.assertEqual(
            blocks,
            BlockType.PARAGRAPH
        )

if __name__ == "__main__":
    unittest.main()