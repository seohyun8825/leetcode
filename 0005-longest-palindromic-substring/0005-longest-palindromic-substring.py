class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expandAroundCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        # 문자열 길이가 1이거나 이미 팰린드롬인 경우
        if len(s) < 2 or s == s[::-1]:
            return s

        longest = ""

        for i in range(len(s)):
            # 홀수
            palindrome1 = expandAroundCenter(i, i)
            # 짝수
            palindrome2 = expandAroundCenter(i, i + 1)


            if len(palindrome1) > len(longest):
                longest = palindrome1
            if len(palindrome2) > len(longest):
                longest = palindrome2

        return longest