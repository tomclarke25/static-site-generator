def markdown_to_blocks(markdown):
    return [blocks for blocks in markdown.split("\n\n") if blocks != ""]