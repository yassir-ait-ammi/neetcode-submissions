class Solution:
    def search(self, nums: List[int], target: int) -> int:
        hight = len(nums) - 1
        low = 0
        while low <= hight:
            mid = int(low + (hight - low) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                hight = mid - 1
        return -1
        