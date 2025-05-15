import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_ne(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
        
    def test_ne_different_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("Different text", TextType.BOLD)
        self.assertNotEqual(node, node2)
        
    def test_ne_different_url(self):
        node = TextNode("This is a text node", TextType.LINKS, "https://example.com")
        node2 = TextNode("This is a text node", TextType.LINKS, "https://different.com")
        self.assertNotEqual(node, node2)
        
    def test_eq_with_url(self):
        node = TextNode("This is a text node", TextType.LINKS, "https://example.com")
        node2 = TextNode("This is a text node", TextType.LINKS, "https://example.com")
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()