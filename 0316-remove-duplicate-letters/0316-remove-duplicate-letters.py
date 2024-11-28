class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        char_count = {char : 0 for char in s}
        for char in s:
            char_count[char] += 1
        

        stack  = []
        visited = set()
        #cbacdcbc
        #c 4 b 2 a 1 d1
        for char in s:
            char_count[char] -=1
            
            if char in visited:
                continue
            while stack and char< stack[-1] and char_count[stack[-1]] > 0:
                visited.remove(stack.pop())

            stack.append(char)
            visited.add(char)

        return ''.join(stack)
