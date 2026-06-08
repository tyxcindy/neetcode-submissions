class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        orig_idx = {}
        for index, value in enumerate(nums):
            orig_idx.setdefault(value, set())
            orig_idx[value].add(index)

        sorted_nums = sorted(nums)

        start = 0
        end = len(sorted_nums) - 1

        while sorted_nums[start] + sorted_nums[end] != target:
            total = sorted_nums[start] + sorted_nums[end]
            if total > target:
                end -= 1
            elif total < target:
                start += 1

        return sorted([orig_idx[sorted_nums[start]].pop(), orig_idx[sorted_nums[end]].pop()])