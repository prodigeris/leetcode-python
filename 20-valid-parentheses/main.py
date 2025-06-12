class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        char_map = {
            "{": "}",
            "[": "]",
            "(": ")"
        }
        for char in s:
            if char in char_map:
                stack.append(char)
            else:
                if len(stack) < 1:
                    return False
                last = stack.pop()
                if char != char_map[last]:
                    return False
        return len(stack) == 0

