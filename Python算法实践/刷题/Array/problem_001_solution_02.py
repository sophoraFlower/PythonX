# 数字1~100放在含有1001个元素的数组中，其中只有唯一的一个元素值重复，其他数字均只出现一次
# 设计一个算法，将重复元素找出来，要求每个数组元素只能访问一次，不使用辅助存储空间

# 累加求和法：将数组中的所有N+1项元素相加，然后减去1+2+3+......+N的和，差即为重复的元素值
# 时间复杂度:O(n)
# 空间复杂度:O(1)
def findDup(array):
    if None==array:
        return -1
    lens = len(array)
    sumArray = 0
    for i in range(lens):
        sumArray += array[i]
    sumN = lens*(lens+1)//2
    value = sumArray-sumN
    if value != 0:
        return abs(value)
    return -1

if __name__ == "__main__":
    array = [1,3,4,2,5,3]
    print(findDup(array))
