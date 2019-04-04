# 数字1~100放在含有1001个元素的数组中，其中只有唯一的一个元素值重复，其他数字均只出现一次
# 设计一个算法，将重复元素找出来，要求每个数组元素只能访问一次，不使用辅助存储空间

# 异或法：异或运算，当相同的元素异或时，其运算结果为0，当不同的元素异或时，其运算结果为非0
# 任何数与数字0进行异或时，其运算结果为该数
# 时间复杂度:O(n)
# 空间复杂度:O(1)
def findDup(array):
    if None==array:
        return -1
    lens = len(array)
    result = 0
    i = 0
    while i<lens:
        result^=array[i]  # result = 0^1^3^4^2^5^3
        i+=1
    j=1
    while j<lens:
        result^=j  # result= 1^2^3^4^5^0^1^3^4^2^5^3 = 0^0^3^0^0 = 3
        j+=1
    return result

if __name__ == "__main__":
    array = [1,3,4,2,5,3]
    print(findDup(array))