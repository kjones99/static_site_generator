import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node1 = HTMLNode('a very real tag', 'wash ufizi drive me to firenze', props={'href': 'https://www.phish.net', 'googly' : 1234})
        node1_repr_str = 'tag: a very real tag\ntext: wash ufizi drive me to firenze\n href="https://www.phish.net" googly="1234"\n'
        self.assertEqual(repr(node1), node1_repr_str)

    def test_repr_with_children(self):
        node1 = HTMLNode('<p>', 'wash ufizi drive me to firenze', props={'href': 'https://www.phish.net', 'googly' : 1234})
        node1_repr_str = 'tag: <p>\ntext: wash ufizi drive me to firenze\n href="https://www.phish.net" googly="1234"\n'
        node2 = HTMLNode('<p>', 'wash ufizi drive me to firenze', [node1],{'href': 'https://www.phish.net', 'googly' : 1234})
        node2_repr_str = f'{node1_repr_str}Child HTML Nodes\n{node1_repr_str}'
        self.assertEqual(repr(node2), node2_repr_str)

    def test_props_to_html(self):
        node1 = HTMLNode(props={'mmorpg': 'https://www.WorldofWarcraft.com', 'myivl' : 721})
        node2 = HTMLNode('<p>', 'wash ufizi drive me to firenze', props={'mmorpg': 'https://www.WorldofWarcraft.com', 'myivl' : 721})
        self.assertEqual(node1.props_to_html(), node2.props_to_html())

    def test_not_equal_props(self):
        node1 = HTMLNode('<p>', 'wash ufizi drive me to firenze', props={'href': 'https://www.phish.net', 'googly' : 1234})
        node2 = HTMLNode('<p>', 'wash ufizi drive me to firenze', props={'href': 'https://www.phish.com', 'googly' : 1234})
        self.assertNotEqual(node1.props_to_html(), node2.props_to_html)


if __name__ == "__main__":
    unittest.main()