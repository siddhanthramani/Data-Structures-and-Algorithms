class ProductNode:

    # we do not define default values for left and right for productNode and plusnode
    # because their values have to be written during the construction of the tree
    # as they are operators and will always NEVER be the leaf node
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() * self.right.eval()

    def inorder(self):
        return "(" + self.left.inorder() + " * " + self.right.inorder() + ")"


class PlusNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() + self.right.eval()

    def inorder(self):
        return "(" + self.left.inorder() + " + " + self.right.inorder() + ")"


class MinNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() - self.right.eval()

    def inorder(self):
        return "( " + self.left.inorder() + " - " + self.right.inorder() + " )"


class NumNode:

    # No left or right is defined as the operands(Numbers) are always leaf nodes
    def __init__(self, num):
        self.num = num

    def eval(self):
        return self.num

    def inorder(self):
        # operands will always be the leaves of the tree
        return str(self.num)


def main():
    p = PlusNode(NumNode(5), NumNode(4))
    s = ProductNode(p, NumNode(6))
    root = PlusNode(s, NumNode(3))

    print(root.eval())
    # the eval used here is the in-built function eval used to evaluate the inorder expression
    print(eval(root.inorder()))


if __name__ == "__main__":
    main()
