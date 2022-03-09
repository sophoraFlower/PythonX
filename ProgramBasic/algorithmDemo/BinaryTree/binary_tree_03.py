def up_adjust(array=None):
    """ 二叉树尾节点的上浮操作 """
    if array is None:
        array = []
    child_index = len(array)-1  # 尾节点索引
    parent_index = (child_index-1)//2  # 父节点索引
    temp = array[child_index]  # 临时子节点
    # 子节点索引大于0且临时子节点的值小于父节点
    while child_index > 0 and temp < array[parent_index]:
        # 子父节点值交换
        array[child_index] = array[parent_index]
        # 子父节点索引值交换
        child_index = parent_index
        # 新的父节点的索引值由原父节点计算得到
        parent_index = (parent_index-1)//2
        # 将子节点的值（存在temp变量中）赋值给交换后的子节点
    array[child_index] = temp


my_array = list([1, 3, 2, 6, 5, 7, 8, 9, 10, 0])
up_adjust(my_array)
print(my_array)

