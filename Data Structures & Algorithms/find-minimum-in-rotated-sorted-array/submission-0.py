class Solution:
    def findMin(self, nums: List[int]) -> int:
        left_ptr = 0
        right_ptr = len(nums) - 1

        while left_ptr <= right_ptr:
            middle_ptr = (left_ptr + right_ptr) // 2

            if nums[left_ptr] <= nums[middle_ptr] <= nums[right_ptr]:
                return nums[left_ptr]
            else:
                if nums[middle_ptr] > nums[right_ptr]:
                    left_ptr = middle_ptr
                else:
                    right_ptr = middle_ptr

            if abs(right_ptr - left_ptr) == 1:
                if nums[left_ptr] < nums[right_ptr]:
                    return nums[left_ptr]
                else:
                    return nums[right_ptr]

        return None