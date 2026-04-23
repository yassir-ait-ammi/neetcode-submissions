class TimeMap:

    def __init__(self):
        self.table = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.table:
            self.table[key] = []
        self.table[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.table:
            return ""
        arr = self.table[key]
        low = 0
        hight = len(arr) - 1
        res = ""
        while low <= hight:
            mid = (low + hight) // 2
            if arr[mid][1] <= timestamp:
                res = arr[mid][0]
                low = mid + 1
            else:
                hight = mid - 1
        return res