# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        arr = []
        temp = head
        k = 1
        while temp:
            if  k >= left and k <= right:
                arr.append(temp.val)
            temp = temp.next
            k += 1
        print(arr)
        up_arr = arr[::-1]
        print(up_arr)

        curr = head
        i = 0
        j = 1
        while curr:
            if j >= left and j <= right:
               curr.val = up_arr[i]
               i += 1
            curr = curr.next
            j += 1

        return head 
        
                
        