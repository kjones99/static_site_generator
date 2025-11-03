import unittest
from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_grandchild_props(self):
        grandchild_node = LeafNode("b", "grandchild", {1337 : 'code', 'mynameis' : 'slim shady'})
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            '<div><span><b 1337="code" mynameis="slim shady">grandchild</b></span></div>',
        )

    def test_five_nested_nodes(self):
        grandchild_node = LeafNode("giant", "I smell the blood of an english man", {1337 : 'code', 'mynameis' : 'slim shady'})
        child_node = ParentNode("fum", [grandchild_node])
        parent_node = ParentNode("fo", [child_node])
        grandparent_node = ParentNode("fi", [parent_node])
        great_grand_parent_node = ParentNode("fee", [grandparent_node])
        self.assertEqual(
            great_grand_parent_node.to_html(),
            '<fee><fi><fo><fum><giant 1337="code" mynameis="slim shady">I smell the blood of an english man</giant></fum></fo></fi></fee>',
        )

    def test_same_node_nested_twice(self):
        grandchild_node = LeafNode("giant", "I smell the blood of an english man", {1337 : 'code', 'mynameis' : 'slim shady'})
        child_node = ParentNode("fum", [grandchild_node])
        parent_node = ParentNode("fo", [child_node, child_node])
        self.assertEqual(
            parent_node.to_html(),
            '<fo><fum><giant 1337="code" mynameis="slim shady">I smell the blood of an english man</giant></fum><fum><giant 1337="code" mynameis="slim shady">I smell the blood of an english man</giant></fum></fo>',
        )

if __name__ == "__main__":
    unittest.main()