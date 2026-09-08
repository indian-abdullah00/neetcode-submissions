# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pointer = None
        start = head
        count = 1
        element = head

        if head.next is None:
            if n == 1:
                head = None
                return head
            if n== 0:
                return start
        while head:
            # print(count)
            if count >= n+1:
                pointer = element
                if element:
                    element = element.next
            count += 1
            head = head.next
        if count-1 == n:
            start = start.next
            return start
        pointer.next = pointer.next.next

        return start
                    
            
        