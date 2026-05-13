# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def search(head, low, high) -> bool:
            if not head:
                return True
            if not low < head.val < high:
                return False
            return search(head.left, low, head.val) and search(head.right, head.val, high)
        return search(root, float('-inf'), float('+inf'))