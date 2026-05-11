# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def move(head : TreeNode, number) -> int:
            if not head:
                return 0
            count = 0
            if  head.val >= number:
                count += 1
            number = max(number, head.val)
            count += move(head.right, number)
            count += move(head.left, number)
            return count
        return move(root, root.val)
        