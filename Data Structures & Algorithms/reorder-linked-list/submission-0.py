# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import ceil

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 0
        start = head

        while start:
            length += 1
            start = start.next
        
        left = head
        right = head

        i = 0
        while  i < ceil(length/2):
            i += 1
            prev = right
            right = right.next

        prev.next =None

        prev = None
        curr = right

        print(right, curr)
        while curr:
            temp = curr.next 
            curr.next = prev
            prev = curr
            curr = temp
        
        right = prev
        
        while left and right:
            print("hi")
            temp_right = right.next
            temp_left = left.next

            right.next = temp_left
            left.next = right

            right = temp_right
            left = temp_left
      





            

        
