# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        current = slow.next
        slow.next = None
        prev = None
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            
        
        while prev:
            fir_temp = head.next
            sec_temp = prev.next

            head.next = prev
            prev.next = fir_temp

            head = fir_temp
            prev = sec_temp
        
        return prev
        

