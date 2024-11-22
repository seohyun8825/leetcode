class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)  
        result = [1] * n  # [1,1,1,1,,]

        # 왼쪽 곱
        left_product = 1
        for i in range(n):
            result[i] = left_product  
            left_product *= nums[i]  #[1,1,2,6]

        # 오른쪽 곱 
        right_product = 1
        for i in range(n - 1, -1, -1):  
            result[i] *= right_product  
            right_product *= nums[i]  

        return result
