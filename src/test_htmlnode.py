import unittest
from htmlnode import HTMLNode
from textnode import TextNode, TextType


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("div", "This is a div", [TextNode("This is a text node", TextType.BOLD)], {"class": "container"})
        node2 = HTMLNode("div", "This is a div", [TextNode("This is a text node", TextType.BOLD)], {"class": "container"})
        self.assertEqual(node, node2)

    def test_ne(self):
        node = HTMLNode("div", "This is a div", [TextNode("This is a text node", TextType.BOLD)], {"class": "container"})
        node2 = HTMLNode("div", "This is a div", [TextNode("This is a text node", TextType.BOLD)], {"class": "different"})
        self.assertNotEqual(node, node2)

    def test_ne_different_tag(self):
        node = HTMLNode("div", "This is a div", [TextNode("This is a text node", TextType.BOLD)], {"class": "container"})
        node2 = HTMLNode("span", "This is a div", [TextNode("This is a text node", TextType.BOLD)], {"class": "container"})
        self.assertNotEqual(node, node2)

    def test_ne_different_value(self):
        node = HTMLNode("div", "This is a div", [TextNode("This is a text node", TextType.BOLD)], {"class": "container"})
        node2 = HTMLNode("div", "This is a different div", [TextNode("This is a text node", TextType.BOLD)], {"class": "container"})
        self.assertNotEqual(node, node2)


if __name__ == '__main__':
    unittest.main()
