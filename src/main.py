from textnode import TextType
from textnode import TextNode
from leafnode import LeafNode
from enum import Enum

def main():
    my_node = TextNode("wash ufizi drive me to firenze", TextType.LINKS, "https://www.boot.dev")
    print(my_node)

if __name__ == "__main__":
    main()