class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mp = [0] * len(temperatures)
        for left in range (len(temperatures)):
            # right = left + 1
            for right in range(left, len(temperatures)):
                if temperatures[left] < temperatures[right]:
                    mp[left] = right - left
                    break
            if right >= len(temperatures):
                mp[left] = 0
        return mp