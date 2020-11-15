class Node:
    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        """
        Compare the new value with the parent node
        :param data:
        :return:
        """
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def print_tree(self):
        """
        Print the tree
        :return:
        """
        if self.left:
            self.left.print_tree()
        print(self.data),
        if self.right:
            self.right.print_tree()

    def height(self, node):
        """
        height of the tree
        :return:
        """
        if node.left == None or node.right == None:
            return 1
        lh = self.height(node.left)
        rh = self.height(node.right)
        return 1 + max(lh + rh)

root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)

root.print_tree()

print(root.height(root))