import unittest
from textnode import TextNode, TextType
from splitfuncs import extract_markdown_links, extract_markdown_images, split_nodes_image, split_nodes_link, text_to_textnodes

class TestTextSplitting(unittest.TestCase):

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_images_again(self):
        node = TextNode(
            "Never![gonna](giveyouup.com) never gonna ![let](youdown.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Never", TextType.TEXT),
                TextNode("gonna", TextType.IMAGE, "giveyouup.com"),
                TextNode(" never gonna ", TextType.TEXT),
                TextNode(
                    "let", TextType.IMAGE, "youdown.com"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links_again(self):
        node = TextNode(
            "Never[gonna](giveyouup.com) never gonna [let](youdown.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Never", TextType.TEXT),
                TextNode("gonna", TextType.LINK, "giveyouup.com"),
                TextNode(" never gonna ", TextType.TEXT),
                TextNode(
                    "let", TextType.LINK, "youdown.com"
                )
            ],
            new_nodes,
        )

    def test_text_to_textnodes(self):
        text = 'This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'
        new_nodes = text_to_textnodes(text)
        self.assertEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            new_nodes
        )

    def test_text_to_textnodes_again(self):
        text = '**text** _with_ an italic word and a ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) `and a` [link](https://boot.dev)'
        new_nodes = text_to_textnodes(text)
        self.assertEqual(
            [
                TextNode("text", TextType.BOLD),
                TextNode(" ", TextType.TEXT),
                TextNode("with", TextType.ITALIC),
                TextNode(" an italic word and a ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" ", TextType.TEXT),
                TextNode("and a", TextType.CODE),
                TextNode(" ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            new_nodes
        )

    def test_text_trailing_link(self):
        text = '**text** _with_ an italic word and a ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) `and a` [link](https://boot.dev) woohoo'
        new_nodes = text_to_textnodes(text)
        self.assertEqual(
            [
                TextNode("text", TextType.BOLD),
                TextNode(" ", TextType.TEXT),
                TextNode("with", TextType.ITALIC),
                TextNode(" an italic word and a ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" ", TextType.TEXT),
                TextNode("and a", TextType.CODE),
                TextNode(" ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" woohoo", TextType.TEXT)
            ],
            new_nodes
        )

    def test_text_trailing_image(self):
        text = '**text** _with_ an italic word and a ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) are we done testing yet?'
        new_nodes = text_to_textnodes(text)
        self.assertEqual(
            [
                TextNode("text", TextType.BOLD),
                TextNode(" ", TextType.TEXT),
                TextNode("with", TextType.ITALIC),
                TextNode(" an italic word and a ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" are we done testing yet?", TextType.TEXT),
            ],
            new_nodes
        )

    def test_text_starting_with_link(self):
        text = '[link](https://boot.dev) is a pretty fun `coding` _platform_ ![I mean look at this guy](https://imgur.com/t/bear) I think i might get **good** at this'
        new_nodes = text_to_textnodes(text)
        self.assertEqual(
            [
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" is a pretty fun ", TextType.TEXT),
                TextNode("coding", TextType.CODE),
                TextNode(" ", TextType.TEXT),
                TextNode("platform", TextType.ITALIC),
                TextNode(" ", TextType.TEXT),
                TextNode("I mean look at this guy", TextType.IMAGE, "https://imgur.com/t/bear"),
                TextNode(" I think i might get ", TextType.TEXT),
                TextNode("good", TextType.BOLD),
                TextNode(" at this", TextType.TEXT),
            ],
            new_nodes
        )


if __name__ == "__main__":
    unittest.main()