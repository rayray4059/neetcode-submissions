# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge(list1, list2):
            dummy = ListNode()
            current = dummy

            while list1 and list2:
                if list1.val <= list2.val:
                    current.next = list1
                    list1 = list1.next
                    current = current.next
                else:
                    current.next = list2
                    list2 = list2.next
                    current = current.next
                
            if list1:
                current.next = list1
            else:
                current.next = list2
                
            return dummy.next
        
        if len(lists) == 0:
            return None
        
        out = lists[0]

        for l in lists[1:]:
            out = merge(out, l)
        
        return out

