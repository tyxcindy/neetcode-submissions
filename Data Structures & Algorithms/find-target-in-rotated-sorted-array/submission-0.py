class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ## EDGE CASES ##
        length = len(nums)
        first = nums[0]
        last = nums[length - 1]
        if (length == 1 and first != target) or (target < first and target > last):
            return -1

        ## BINARY SEARCH ##
        left_ptr = 0
        right_ptr = length - 1

        while right_ptr - left_ptr > 1:
            middle_ptr = (left_ptr + right_ptr) // 2
            left = nums[left_ptr]
            middle = nums[middle_ptr]

            if left < middle:
                if left <= target <= middle:
                    right_ptr = middle_ptr
                else:
                    left_ptr = middle_ptr + 1
            else: ## middle < right
                if middle <= target <= nums[right_ptr]:
                    left_ptr = middle_ptr
                else:
                    right_ptr = middle_ptr - 1
                        
        if target == nums[left_ptr]:
            return left_ptr
        elif target == nums[right_ptr]:
            return right_ptr
        else:
            return -1