class BinarySearchTree:
    # this is a node class which is internal to the BST
    class __Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

        def getVal(self):
            return self.val

        def getLeft(self):
            return self.left

        def getRight(self):
            return self.right

        def setVal(self, newval):
            self.val = newval

        def setLeft(self, newleft):
            self.left = newleft

        def setRight(self, newright):
            self.right = newright

        # returns the inorder traveresal
        # this performs a recursive traveresal of the tree
        def __iter__(self):
            # the for elem in self.left returns a tree which has been traversed in order
            # this is a recursive function
            # self.left is a subtree, therefore elem is the node of the new subtree
            # self.left is called on this node and this keeps going till we hit a leaf node
            # which returns the value of the node
            # self.right will be providing the right traversal values of each subtree
            # Through this, we will thus get the inorder traversal of the BST

            # while above is the way IT SHOULD PROBABLY work
            # I dont actually understand how the recursion takes place without recalling the __iter
            # method

            if self.left != None:
                for elem in self.left:
                    yield elem

            # returns the value of self node
            yield self.val

            # returns the right element. IF the right element is a list or a dict, returns all
            # the values of the right list
            if self.right != None:
                for elem in self.right:
                    yield elem

    # Below are the methods of the BST Class

    def __init__(self):
        self.root = None

    def insert(self, val):

        # the __insert function is not passed as a self parameter. It is
        # a static function(not a method of the class) but is hidden inside the
        # insert function so users of the class will not know it exists

        def __insert(root, val):

            # if the root is none, then that it means nothing exists
            # so we create a BST Node and enter the values as val
            # we then return this node as the root of self
            if root == None:
                return BinarySearchTree.__Node(val)

            # if the root already exists and we want to add an new value
            # depending whether the value is smaller or larger, we pass
            # get the left value(node) or right value(node) of root node and
            # call the __insert function recursively
            # the function keeps going till the it hits the location where the value has to
            # be entered. At this point, the root at that point would be None, and a node will be
            # created and the inserted value is stored in that node

            if val < root.getVal():
                root.setLeft(__insert(root.getLeft(), val))

            else:
                root.setRight(__insert(root.getRight(), val))

            # after inserting, we return the root of the BST
            return root

        self.root = __insert(self.root, val)

    # to iterate through the BST

    def __iter__(self):
        if self.root != None:
            return self.root.__iter__()
        else:
            return [].__iter__()


def main():

    x = input("Enter a list of numbers : ")
    lst = x.split()

    tree = BinarySearchTree()

    for num in lst:
        tree.insert(float(num))

    for num in tree:
        print(num)


if __name__ == "__main__":
    main()
