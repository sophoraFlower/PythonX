"""
二叉搜索树(BST)是一棵树，其所有节点都遵循下述属性 - 节点的左子树的键小于或等于其父节点的键。
节点的右子树的键大于其父节点的键。 因此，BST将其所有子树分成两部分; 左边的子树和右边的子树，可以定义为
    left_subtree (keys)  ≤  node (key)  ≤  right_subtree (keys)
"""


class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

# Insert method to create nodes
    def insert(self, data):

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


# findval method to compare the value with nodes
    def find_val(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+" Not Found"
            return self.left.find_val(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+" Not Found"
            return self.right.find_val(lkpval)
        else:
            print(str(self.data) + ' is found')


# Print the tree
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print( self.data),
        if self.right:
            self.right.print_tree()


root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
print(root.find_val(7))
print(root.find_val(14))
print(root.print_tree())
