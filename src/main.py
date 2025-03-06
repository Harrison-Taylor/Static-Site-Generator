from textnode import *
def main():
    testnode = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    test = testnode.__repr__()
    print(f"{test}")

main()