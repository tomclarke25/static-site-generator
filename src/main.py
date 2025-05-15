from src.inline_markdown import split_nodes_delimiter, split_nodes_image
from textnode import TextNode, TextType

def main():
    # print(TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev").__repr__())
    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    print(new_nodes)


if __name__ == "__main__":
    main()
