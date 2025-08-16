# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        cur = head
        array = []
        
        while cur:
            array.append(cur.val)
            cur = cur.next

        final = len(array) - n        
        
        if head.next == None:
            return None

        i = 0
        temp = head
        prev = None

        while temp:
            if i == final:
                if prev == None:
                    head = temp.next
                elif temp.next != None:
                   prev.next = temp.next
                else:
                   prev.next = None
                break         
            prev = temp
            temp = temp.next
            i += 1

        return head
             
                
            
            




        