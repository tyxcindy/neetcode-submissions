# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Finding Middle Node
        slow = head 
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        fast = slow.next
        slow.next = None

        # Reversing Second Half
        node = None

        while fast:
            new_head = fast.next
            fast.next = node
            node = fast
            fast = new_head
        
        # Merging Linked List
        first_start = head
        second_start = node

        while first_start and second_start:
            temp = first_start.next
            first_start.next = second_start
            temp2 = second_start.next
            first_start.next.next = temp
            second_start = temp2
            first_start = temp
                
        
