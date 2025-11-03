import unittest
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_p_with_props(self):
        node = LeafNode("p", "Hello, world!", {'href': 'https://www.phish.net', 'googly' : 1234})
        self.assertEqual(node.to_html(), '<p href="https://www.phish.net" googly="1234">Hello, world!</p>')

    def test_leaves_no_tag(self):
        node1 = LeafNode(None, "Hello, world!", {'href': 'https://www.phish.net', 'googly' : 1234})
        node2 = LeafNode(None, "Hello, world!")
        self.assertEqual(node1.to_html(), node2.to_html())

if __name__ == "__main__":
    unittest.main()