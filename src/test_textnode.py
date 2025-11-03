import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)


    def test_eq_with_url(self):
        node1 = TextNode("wash ufizi drive me to firenze", TextType.LINK, "phish.net")
        node2 = TextNode("wash ufizi drive me to firenze", TextType.LINK, "phish.net")
        self.assertEqual(node1, node2)

    def test_diff_text(self):
        node1 = TextNode("wash ufizi drive me to firenze", TextType.LINK, "phish.net")
        node2 = TextNode("you feed from the bottom", TextType.LINK, "phish.net")
        self.assertNotEqual(node1, node2)

    def test_diff_text_type(self):
        node1 = TextNode("wash ufizi drive me to firenze", TextType.IMAGE, "phish.net")
        node2 = TextNode("wash ufizi drive me to firenze", TextType.LINK, "phish.net")
        self.assertNotEqual(node1, node2)

    def test_diff_url(self):
        node1 = TextNode("wash ufizi drive me to firenze", TextType.IMAGE, "phish.net")
        node2 = TextNode("wash ufizi drive me to firenze", TextType.LINK, "phish.com")
        self.assertNotEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()