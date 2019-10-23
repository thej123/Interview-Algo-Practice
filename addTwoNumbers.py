# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        output = ListNode(None)
        temp = output
        addOne = False
        
        while (l1 or l2):
            a = 0
            if l1:
                a += l1.val
                l1 = l1.next
                
            if l2:
                a += l2.val
                l2 = l2.next
            
            if addOne:
                a += 1
                addOne = False
            if a > 9:
                a = a % 10
                addOne = True
            
            temp.next = ListNode(a)
            temp = temp.next
        
        if addOne:
            temp.next = ListNode(1)
        return output.next
