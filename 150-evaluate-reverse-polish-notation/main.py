from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                print(a, token, b)
                if token == '+':
                    stack.append(a + b)
                if token == '-':
                    stack.append(a - b)
                if token == '*':
                    stack.append(a * b)
                if token == '/':
                    stack.append(a // b)
                print(stack)
        return stack[0]


print(Solution().evalRPN(["4", "13", "5", "/", "+"]))
