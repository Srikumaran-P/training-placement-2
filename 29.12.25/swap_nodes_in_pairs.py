# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        prev = None
        prev_tail = None

        while curr and curr.next:
            prev = curr 
            curr = curr.next

            # swap
            prev.next = curr.next
            curr.next = prev

            if prev_tail:
                prev_tail.next = curr
            else:
                head = curr
            
            prev_tail = prev
            curr = prev.next
        
        return head


