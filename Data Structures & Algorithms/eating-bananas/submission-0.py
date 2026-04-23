class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        hight = max(piles)
        while low <= hight:
            mid = (hight + low) // 2
            hours = sum((pile + mid - 1) // mid for pile in piles)
            print(hours)
            if hours > h:
                low = mid + 1
            else:
                hight = mid - 1
        return low
