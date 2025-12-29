# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        dummy= ListNode()
        curr= dummy
        for i in lists:

            while i:
                curr.next= i
                i= i.next
                curr= curr.next
        
        res=[]
        curr= dummy.next
        while curr:
            res.append(curr.val)
            curr= curr.next
        
        res.sort()

        final_answer= ListNode()
        current= final_answer

        for i in res:
            current.next= ListNode(i)
            current= current.next

        return final_answer.next
