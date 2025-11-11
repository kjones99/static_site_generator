import unittest
from markdownconverting import markdown_to_html_node



class TestMarkdownConverting(unittest.TestCase):

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_code_block(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_heading_block(self):
        md = """
##### 
This is text that _should_ not remain
the **same** even with inline stuff
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h5>This is text that <i>should</i> not remain\nthe <b>same</b> even with inline stuff</h5></div>",
        )

    def test_quote_block(self):
        md = """
>This is text that _should_ not remain
>the **same** even with inline stuff
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is text that <i>should</i> not remain\nthe <b>same</b> even with inline stuff</blockquote></div>",
        )

    def test_ordered_list_block(self):
        md = """
1. This is text that _should_ not remain
2. the **same** even with inline stuff
3. Wash ufizi `drive me to` **firenze**
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is text that <i>should</i> not remain</li><li>the <b>same</b> even with inline stuff</li><li>Wash ufizi <code>drive me to</code> <b>firenze</b></li></ol></div>",
        )

    def test_unordered_list_block(self):
        md = """
- This is text that _should_ not remain
- the **same** even with inline stuff
- Wash ufizi `drive me to` **firenze**
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is text that <i>should</i> not remain</li><li>the <b>same</b> even with inline stuff</li><li>Wash ufizi <code>drive me to</code> <b>firenze</b></li></ul></div>",
        )

if __name__ == "__main__":
    unittest.main()