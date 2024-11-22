class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_num = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in map_num:
                return[map_num[complement], i]
            map_num[num] = i