# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        firstNumber = 0
        secondNumber = 0
        curr = head
        prev = None
        while curr is not None:
            if firstNumber - secondNumber >= n:
                if prev is None:
                    prev = head
                else:
                    prev = prev.next
                secondNumber += 1
            firstNumber += 1
            curr = curr.next
        if prev is None:
            return head.next
        if prev.next:
            prev.next = prev.next.next
        return head