def up_adjust(array=None):
    """ 二叉树尾节点的上浮操作 """
    if array is None:
        array = []
    child_index = len(array)-1  # 尾节点索引
    parent_index = (child_index-1)//2  # 父节点索引
    temp = array[child_index]  # 临时子节点
    # 子节点索引大于0且临时子节点的值小于父节点：即子父比较
    while child_index > 0 and temp < array[parent_index]:
        # 子父节点值交换
        array[child_index] = array[parent_index]
        # 子父节点索引值交换
        child_index = parent_index
        # 新的父节点的索引值由原父节点计算得到
        parent_index = (parent_index-1)//2
        # 将子节点的值（存在temp变量中）赋值给交换后的子节点
    array[child_index] = temp


def down_adjust(parent_index, length, array=None):
    """
    二叉树的下沉操作
    :param parent_index：待下沉的节点坐标
    :param length： 堆的长度范围
    :param array：原数组
    """
    # temp保存父节点的值，用于最后的赋值
    if array is None:
        array = []
    temp = array[parent_index]
    child_index = 2 * parent_index + 1
    while child_index < length:
        # 比较当前节点的左右节点
        if child_index+1 < length and array[child_index+1] < array[child_index]:
            child_index += 1
        # 比较当前节点和左右节点中的最小的一个
        if temp <= array[child_index]:
            break
        # 当前节点与子节点交换
        array[parent_index] = array[child_index]
        parent_index = child_index
        child_index = 2 * child_index + 1
    array[parent_index] = temp


def build_heap(array=None):
    if array is None:
        array = []
    #
    for i in range((len(array)-2)//2, -1, -1):
        down_adjust(i, len(array), array)


my_array = list([1, 3, 2, 6, 5, 7, 8, 9, 10, 0])
up_adjust(my_array)
print(my_array)
my_array_02 = list([6, 3, 1, 5, 8, 9, 7, 10, 2])
build_heap(my_array_02)
print(my_array_02)
