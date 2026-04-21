class Solution:
    def is_integer(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            print(stack)
            if (self.is_integer(tokens[i])):
                stack.append(int(tokens[i]))
            elif (tokens[i] == '*'):
                a = stack.pop()
                b = stack.pop()
                stack.append(a * b)
            elif (tokens[i] == '+'):
                a = stack.pop()
                b = stack.pop()
                stack.append(a + b)
            elif (tokens[i] == '-'):
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif (tokens[i] == '/'):
                a = stack.pop()
                b = stack.pop()
                if (a != 0):
                    stack.append(int(b / a))
        return stack[-1]