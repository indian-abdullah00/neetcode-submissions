class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        num1, num2 = "",""
        while l1:
            num1 = num1 + str(l1.val)
            l1 = l1.next
        
        while l2:
            num2 = num2 + str(l2.val)
            l2 = l2.next
        
        num1 = num1[::-1]
        num2 = num2[::-1]

        num3 = int(num1) + int(num2)
        print(str(num3)[::-1])
        count = 0
        for i in str(num3)[::-1]  :
            if count == 0:
                head = ListNode(int(i))
                list1 = head
                
                count = 1
                continue

            list1.next = ListNode(int(i))
            list1 = list1.next
        return head
            

            

