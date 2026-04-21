class MinStack:

    def __init__(self):
        self.mp = []

    def push(self, val: int) -> None:
        self.mp.append(val)

    def pop(self) -> None:
        self.mp.pop()

    def top(self) -> int:
        return self.mp[-1]

    def getMin(self) -> int:
        if not self.mp:
            return 0
        result = self.mp[0]
        for i in range(len(self.mp)):
            if (self.mp[i] < result):
                result = self.mp[i]
        return result