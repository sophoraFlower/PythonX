from queue import Queue

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


def pre_order_traversal_with_stack(node):
    stack = []
    while node is not None or len(stack) > 0:
        while node is not None:
            print(node.data)
            stack.append(node)
            node = node.left
        if len(stack) > 0:
            node = stack.pop()
            node = node.right


def level_order_traversal(node):
    queue = Queue()
    queue.put(node)
    while not queue.empty():
        node = queue.get()
        print(node.data)
        if node.left is not None:
            queue.put(node.left)
        if node.right is not None:
            queue.put(node.right)


my_input_list = list([1, 2, 4, None, None, 5, None, None, 3, None, 6])
root = create_binary_tree(my_input_list)
pre_order_traversal_with_stack(root)
level_order_traversal(root)
