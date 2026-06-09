class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return None

        output = [1] * len(nums)

        left = 1
        for i in range(1, len(nums)):
            left *= nums[i - 1]
            output[i] = left

        right = 1
        for i in range(len(nums) - 2, -1, -1):
            right *= nums[i + 1]
            output[i] *= right

        return output