class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0 

        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water_trapped = 0

        while left < right:
            if height[left] < height[right]:
                # 왼쪽이 더 낮은 경우
                if height[left] >= left_max:
                    left_max = height[left] 
                else:
                    water_trapped += left_max - height[left]  # 고인 물
                left += 1
            else:
                # 오른쪽이 더 낮은 경우
                if height[right] >= right_max:
                    right_max = height[right]  # 오른쪽 최대 높이 갱신
                else:
                    water_trapped += right_max - height[right]  # 고인 물
                right -= 1

        return water_trapped
