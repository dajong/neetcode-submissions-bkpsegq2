# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = head

        tmp = []
        while dummy:
            tmp.append(dummy)
            dummy = dummy.next
        
        removeIndex = len(tmp) - n
        if removeIndex == 0:
            return head.next

        tmp[removeIndex - 1].next = tmp[removeIndex].next
        return head

        