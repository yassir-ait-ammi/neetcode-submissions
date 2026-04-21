class Solution:
    def isValid(self, s: str) -> bool:
        mp = []
        for i in range(len(s)):
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