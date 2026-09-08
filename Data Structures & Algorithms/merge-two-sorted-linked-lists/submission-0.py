# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        finish = 0
        pointer1 = None
        pointer2 = None

        if list1:
            if list2:
                if list1.val<=list2.val:
                    prev = list1
                    list1 = list1.next
                else:
                    prev = list2
                    list2 = list2.next
            else:
                prev = list1
                list1 = list1.next
        elif list2:
            prev = list2
            list2 = list2.next
        else:
            prev = None
        start = prev
        
        
        one = True if list1 else False
        two = True if list2 else False
        while one or two:
            if not list1:
                one = False
            if not list2:
                two = False
            
            if one and two:
                if list1.val <= list2.val:
                    curr = list1
                    list1 = list1.next
                else:
                    curr = list2
                    list2 = list2.next
                # define this
                prev.next = curr
                prev = curr
            elif one or two:
                if two:
                    prev.next = list2
                    break
                if one:
                    prev.next = list1
                    break
            else:
                break

        return start

                    
            

            

            

             



        