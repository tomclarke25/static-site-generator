from textnode import TextNode, TextType

def main():
    print(TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev").__repr__())


if __name__ == "__main__":
    main()
