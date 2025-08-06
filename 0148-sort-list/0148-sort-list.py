# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        temp = head 
        result = []

        while temp:
            result.append(temp.val)
            temp = temp.next

        result.sort()

        start = head
        i = 0
        while start:
            start.val = result[i]
            i += 1
            start = start.next
        return head       