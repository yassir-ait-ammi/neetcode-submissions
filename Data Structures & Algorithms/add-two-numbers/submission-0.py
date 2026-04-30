class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_list = None
        curr = None
        left_over = 0

        while l1 is not None or l2 is not None or left_over:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + left_over
            new_node = ListNode(total % 10)
            left_over = total // 10
            if new_list is None:
                new_list = new_node
                curr = new_node
            else:
                curr.next = new_node
                curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return new_list