import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        n1 = TextNode("Text node one", TextType.ITALIC)
        n2 = TextNode("Text node two", TextType.BOLD)
        self.assertNotEqual(n1, n2)

    def test_url_is_not_none(self):
        n1 = TextNode("text 1", TextType.TEXT, url="https://github.com/kajetanw1195")
        n2 = TextNode("text 2", TextType.TEXT, url="https://github.com/kajetanw1195")
        self.assertIsNotNone(n1.url, n2.url)

    def test_url_is_none(self):
        n1 = TextNode("text 1", TextType.CODE, url=None)
        n2 = TextNode("text 2", TextType.CODE, url=None)
        self.assertIsNone(n1.url, n2.url)
        
    def test_text_type(self):
        n = TextNode("text", TextType.LINK)
        self.assertIn(n.text_type, TextType)

    def test_text_type2(self):
        n = TextNode("text", "cursive")
        self.assertNotIn(n.text_type, TextType)
    
    def test_is_instance(self):
        n = TextNode("text", TextType.TEXT)
        self.assertIsInstance(n, TextNode)

    def test_is_not_instance(self):
        n = TextNode("text", TextType.TEXT)
        self.assertNotIsInstance(n, TextType)

    def test_text(self):
        n = TextNode(124513, TextType.CODE, url=None)
        self.assertIsInstance(n.text, int)

    def test_text2(self):
        n = TextNode(124513, TextType.CODE, url=None)
        self.assertNotIsInstance(n.text, str)

if __name__ == "__main__":
    unittest.main()