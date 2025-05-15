class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq__(self, other):
        if isinstance(other, HTMLNode):
            return (self.tag == other.tag
                    and self.value == other.value
                    and self.children == other.children
                    and self.props == other.props
                    )
        return False

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def to_html(self):
        raise NotImplementedError("to_html not implemented")

    def props_to_html(self):
        return " ".join(f"{k}={v}" for k, v in self.props.items())
