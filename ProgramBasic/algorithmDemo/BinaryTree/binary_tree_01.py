class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create_binary_tree(input_list=None):
    """ 构建二叉树 """
    if input_list is None:
        input_list = []
    if input_list is None or len(input_list) == 0:
        return None
    data = input_list.pop(0)
    if data is None:
        return None
    node = TreeNode(data)
    # 使用递归
    node.left = create_binary_tree(input_list)
    node.right = create_binary_tree(input_list)
    return node


def pre_order_traversal(node):
    """ 前序遍历 """
    if node is None:
        return
    print(node.data)
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)
    return node


def in_order_traversal(node):
    """ 中序遍历 """
    if node is None:
        return
    in_order_traversal(node.left)
    print(node.data)
    in_order_traversal(node.right)
    return node


def post_order_traversal(node):
    """ 后序遍历 """
    if node is None:
        return
    post_order_traversal(node.left)
    post_order_traversal(node.right)
    print(node.data)
    return node


my_input_list = list([1, 2, 4, None, None, 5, None, None, 3, None, 6])
root = create_binary_tree(my_input_list)
pre_order_traversal(root)
print("----------------")
in_order_traversal(root)
print("----------------")
post_order_traversal(root)