from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        temp = []
        if nums1[-1] <= nums2[0] | nums1[0] >= nums2[-1]:
            temp = nums1 + nums2
            temp_len = len(temp)
            if temp_len % 2 == 0:
                return (temp[temp_len/2] + temp[(temp_len+2)/2]) /2
            else:
                return temp[(temp_len+1)/2]
        else:
            insert_index =

