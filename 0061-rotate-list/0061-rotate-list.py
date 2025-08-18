# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: find length and tail
        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1
        
        # Step 2: make it circular
        tail.next = head
        
        # Step 3: find new head (n - k % n steps from start)
        k = k % n
        steps_to_new_head = n - k
        
        temp = head
        for _ in range(steps_to_new_head - 1):
            temp = temp.next
        
        new_head = temp.next
        temp.next = None  # break the circle
        
        return new_head
        

        


        
        
        


        