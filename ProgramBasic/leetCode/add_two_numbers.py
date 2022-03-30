from list_node import *


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        result = ListNode(0)
        p = result
        temp = 0

        while l1 and l2:
            p.next = ListNode((l1.val+l2.val+temp) % 10)
            temp = (l1.val+l2.val) // 10
            l1 = l1.next
            l2 = l2.next
            p = p.next

        if l2:
            while l2:
                p.next = ListNode((l2.val+temp) % 10)
                temp = l2.val // 10
                l2 = l2.next
                p = p.next

        if l1:
            while l1:
                p.next = ListNode((l1.val+temp) % 10)
                temp = l1.val // 10
                l1 = l1.next
                p = p.next

        if temp == 1:
            p.next = ListNode(1)

        return result.next




