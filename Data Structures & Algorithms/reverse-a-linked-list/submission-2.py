# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = None
        while head:
            ## Save next head
            next_head = head.next

            ## Switch direction
            head.next = node

            ## Save next tail
            node = head

            ## Continue with next head
            head = next_head

        
        return node     ## node is the new head
        