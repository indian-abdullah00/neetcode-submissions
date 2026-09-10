# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverse(Node,k):

            prev = None
            curr = Node

  
            while k > 0:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                k-=1
            
            # start = prev
            # while start:
            #     print(start.val, end= '->')
            #     start = start.next
            
            return prev

        

        point1 = head
        point2 = head
        real_head = head
        turn = k
        prev = None

        while point2:
            while turn > 0:
                turn -=1
                if point2 is None:
                    return real_head

                point2 = point2.next
                

            turn = k
            new_head = reverse(point1, k)
            if not prev:
                real_head = new_head 

            

            if prev:
                prev.next = new_head
            
            point1.next = point2
            prev = point1
            point1 = point1.next

        return real_head



            


            
            
            

            





    

        

            
        


        