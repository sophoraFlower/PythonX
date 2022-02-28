# 数字1~100放在含有1001个元素的数组中，其中只有唯一的一个元素值重复，其他数字均只出现一次
# 设计一个算法，将重复元素找出来，要求每个数组元素只能访问一次，不使用辅助存储空间

# 空间换时间法，使用了额外的辅助空间
# 时间复杂度:O(n)
# 空间复杂度:O(n)
def findDup(array):
    if None==array:
        return -1
    lens = len(array)
    hashTable = dict()
    i=0
    while i<lens-1:
        hashTable[i]=0
        i+=1
    j=0
    while j<lens:
        if hashTable[array[j]-1] == 0:
            hashTable[array[j]-1] = array[i]-1
        else:
            return array[i]
        j+=1
    return -1

if __name__ == "__main__":
    array = [1,3,4,2,5,3]
    print(findDup(array))

