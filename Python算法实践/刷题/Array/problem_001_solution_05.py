# 数字1~100放在含有1001个元素的数组中，其中只有唯一的一个元素值重复，其他数字均只出现一次
# 设计一个算法，将重复元素找出来，要求每个数组元素只能访问一次，不使用辅助存储空间

# 环形相遇法：构造单链表，转化为“已知一个单链表存在环，找出环的入口点”
# 时间复杂度:O(n)
# 空间复杂度:O(1)
def findDup(array):
    if None==array:
        return -1
    slow = 0
    fast = 0
    while True:
        fast = array[array[fast]]
        slow = array[slow]
        if slow==fast:  # 找到相遇点
            break
    fast=0
    while True:
        fast = array[fast]
        slow = array[slow]
        if slow==fast:  # 找到入口点
            return slow

if __name__ == "__main__":
    array = [1,3,4,2,5,3]
    print(findDup(array))