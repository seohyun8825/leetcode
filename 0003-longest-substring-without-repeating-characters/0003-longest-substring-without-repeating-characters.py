class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        answer = 0
        head = 0

        for i, char in enumerate(s):
            if char in used and head <= used[char]:
                head = used[char]+1
            else:
                answer = max(answer, i - head+1)
            used[char] = i

        return answer