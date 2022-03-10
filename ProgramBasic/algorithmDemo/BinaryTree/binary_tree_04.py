class BinaryTreeNode:
    """ 基于链表 """
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


def create_binary_tree(input_list=None):
    if input_list is None:
        input_list = []
    if input_list is None or len(input_list) == 0:
        return None
    data = input_list.pop(0)
    if data is None:
        return None
    node = BinaryTreeNode(data)
    # 递归模拟: 根节点>左子树>右子树
    node.leftChild = create_binary_tree(input_list)  # 左支树的创建，同树的创建
    node.rightChild = create_binary_tree(input_list)  # 右支树的创建，同树的创建
    return node


def pre_order_traversal(node):
    if node is None:
        return None
    # 根节点 > 左子节点 > 右子节点
    print(node.data)
    # 递归逻辑：遍历左支树，一直遍历到叶子结点
    pre_order_traversal(node.leftChild)
    pre_order_traversal(node.rightChild)
    return node


def in_order_traversal(node):
    if node is None:
        return None
    # 左子节点 > 根节点 > 右子节点
    in_order_traversal(node.leftChild)
    print(node.data)
    in_order_traversal(node.rightChild)
    return node


def post_order_traversal(node):
    if node is None:
        return None
    # 左子节点  > 右子节点 > 根节点
    post_order_traversal(node.leftChild)
    post_order_traversal(node.rightChild)
    print(node.data)
    return node


def pre_order_traversal_with_stack(node):
    # 非递归的方式，利用栈的回溯功能
    # 先序遍历：先遍历根，之后左支树(当左支树为None时，进行出栈操作后进行右支树操作)
    # 当右支树为None时，同样进行出栈操作，并进行左支树操作
    # 出栈的条件：当前节点为None
    # 栈的目的是通过栈的回溯功能回到上一节点，回上一节点前当前节点的左右节点均已遍历
    stack = []
    while node is not None or len(stack) > 0:
        while node is not None:
            print(node.data)
            stack.append(node)
            node = node.leftChild
        if len(stack) > 0:
            node = stack.pop()
            node = node.rightChild
    return node


def in_order_traversal_with_stack(node):
    stack = []
    while node is not None or len(stack) > 0:
        while node is not None:
            stack.append(node)
            node = node.leftChild
        if len(stack) > 0:
            node = stack.pop()
            print(node.data)
            node = node.rightChild
    return node


def post_order_traversal_with_stack(node):
    stack = []
    while node is not None or len(stack) > 0:
        while node is not None:
            stack.append(node)
            if node.leftChild:
                node = node.leftChild
                if node:
                    print(node.data)
            else:
                node = node.rightChild
                if node:
                    print(node.data)
        node = stack.pop()
    return node


# 补None后为完全二叉树的前序遍历 <> list
my_input_list = list([1, 2, 4, None, None, 5, None, None, 3, None, 6])
root = create_binary_tree(my_input_list)
# pre_order_traversal(root)
print("------------")
# in_order_traversal(root)
print("------------")
post_order_traversal(root)
print("------------")
# pre_order_traversal_with_stack(root)
print("------------")
# in_order_traversal_with_stack(root)
print("------------")
post_order_traversal_with_stack(root)
