class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0

        left = 0
        right = len(height) - 1

        while left < right:
            left_height = height[left]
            right_height = height[right]

            area = (right - left) * min(left_height, right_height)

            if area > max_area:
                max_area = area

            if left_height < right_height:
                left += 1
            else:
                right -= 1

        return max_area

        