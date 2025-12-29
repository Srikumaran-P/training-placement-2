# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        temp = head
        total_len = 0
        while temp:
            total_len += 1
            temp = temp.next
        if n == total_len:
            temp = head
            head = head.next
            del temp 
        else:
            temp = head
            curr_len = 0
            while curr_len < total_len - n:
                prev = temp
                temp = temp.next
                curr_len += 1
            prev.next = temp.next
            del temp
        return head
