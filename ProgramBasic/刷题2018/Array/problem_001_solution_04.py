# 数字1~100放在含有1001个元素的数组中，其中只有唯一的一个元素值重复，其他数字均只出现一次
# 设计一个算法，将重复元素找出来，要求每个数组元素只能访问一次，不使用辅助存储空间

# 数据映射法：前驱后继,利用标记作为发现重复数字的关键
# 时间复杂度:O(n)
# 空间复杂度:O(1)
def findDup(array):
    if None==array:
        return -1
    lens = len(array)
    index = 0
    while True:
        if array[index]<0:
            break
        # index=0 > array[0]=1 > 标记array[0]=-1
        # index=1 > array[1]=3 > 标记array[1]=-3
        # index=3 > array[3]=2 > 标记array[3]=-2
        # index=2 > array[2]=4 > 标记array[2]=-4
        # index=4 > array[4]=5 > 标记array[4]=-5
        # index=5 > array[5]=3 > 标记array[5]=-3
        # index=3 > array[3]=-2
        # array[3]<0 break
        # 取反标记
        array[index]*=-1
        # index的后继为arrar[index]
        index = -1*array[index]
        # 越界判断
        if index>=lens:
            print("数组中有非法数字")
            return -1
    return index

if __name__ == "__main__":
    array = [1,3,4,2,5,3]
    print(findDup(array))