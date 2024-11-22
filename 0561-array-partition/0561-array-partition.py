class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        #122566

        return sum(sorted(nums)[::2])