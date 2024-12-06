class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        hash = {}
        count = 0

        for char in stones:
            if char not in hash:
                hash[char] = 1
            else:
                hash[char] += 1

        for char in jewels:
            if char in hash:
                count += hash[char]
        return count