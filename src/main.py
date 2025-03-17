from textnode import TextNode, TextType


def main():
    obj = TextNode("some random text", TextType.LINK, "https://github.com/kajetanw1195")
    print(obj)

main()