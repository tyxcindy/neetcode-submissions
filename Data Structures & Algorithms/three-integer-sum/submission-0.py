class Solution:        
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]

        sorted_nums = sorted(nums)
        length = len(sorted_nums)

        triplets = []
        for i in range(length - 2):
            val = sorted_nums[i]
            if val > 0:
                break
            if i > 0 and val == sorted_nums[i - 1]:
                continue
            else:
                ## TWO SUM SECTION ##
                start = i + 1
                end = len(nums) - 1

                while start < end:
                    start_num = sorted_nums[start]
                    end_num = sorted_nums[end]

                    total = start_num + end_num
                    if total > -val:
                        end -= 1
                    elif total < -val:
                        start += 1
                    elif total == -val:
                        triplets.append([start_num, end_num, val])
                        start += 1
                        end -= 1

                        # Skip duplicates
                        while start < end and sorted_nums[start] == sorted_nums[start - 1]:
                            start += 1
                        
                        while start < end and sorted_nums[end] == sorted_nums[end + 1]:
                            end -= 1
        
        return triplets