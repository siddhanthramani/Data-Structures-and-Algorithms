import queue
from AST_eval import PlusNode, ProductNode, NumNode

# import AST_eval did not work

# we define the prefix expression
# E can stand for any prefix expression


def E(q):
    if q.isEmpty():
        raise ValueError("Invalid Prefix Expression")

    # we get the first entered token (this is always an operator in the prefix form)
    token = q.dequeue()

    # we create a plusnode or a product and give the left and righ values as E(q)
    # the first E(q) will again dequeue the list and will call E(q) again. We will keep building
    # the left part of the tree till we hit the leaf nodes(NumNodes).
    # This is when we come back and build the right side given by the second argument E(q)
    # We keep doing this till we reach the root node

    if token == "+":
        return PlusNode(E(q), E(q))
    if token == "*":
        return ProductNode(E(q), E(q))

    return NumNode(float(token))


def main():
    x = input("Enter prefix expression : ")

    # we get a list of operands and operators in prefix form
    lst = x.split()
    # we create a queue
    q = queue.Queue()

    # we add the operands and operators to the queue
    for token in lst:
        q.enqueue(token)

    # defining the root node as a prefix expresssion E(q)
    # this builds the AST tree on its own
    root = E(q)

    print(root.eval())
    print(root.inorder())


if __name__ == "__main__":
    main()
