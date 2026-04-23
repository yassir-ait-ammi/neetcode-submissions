class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        hight = len(nums) - 1
        while low < hight:
            mid = (hight + low) // 2
            if nums[mid] > nums[hight]:
                low = mid + 1
            else:
                hight = mid
        return nums[low]