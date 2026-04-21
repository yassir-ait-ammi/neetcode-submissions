class Solution:
    def isValid(self, s: str) -> bool:
        mp = []
        lent = len(s)
        for i in range(lent):
            if (s[i] == ']' and len(mp) and mp[-1] == '['):
                mp.pop()
            elif (s[i] == '}' and len(mp) and mp[-1] == '{'):
                mp.pop()
            elif (s[i] == ')' and len(mp) and mp[-1] == '('):
                mp.pop()
            else:
                mp.append(s[i])
        if (len(mp) == 0):
            return True
        return False