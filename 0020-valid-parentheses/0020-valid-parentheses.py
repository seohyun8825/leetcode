class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        val_table = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        for char in s:
            if char not in val_table:
                stack.append(char)

            elif not stack or val_table[char] != stack.pop():
                return False

        return len(stack)==0 