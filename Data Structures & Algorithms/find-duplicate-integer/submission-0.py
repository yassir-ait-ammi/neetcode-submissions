class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        table = []
        for i in range(len(nums)):
            if nums[i] in table:
                return nums[i]
            table.append(nums[i])
        return 0