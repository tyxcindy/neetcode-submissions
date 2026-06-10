class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sorted_num = sorted(set(nums))
        
        length = len(sorted_num)

        maxi = 1
        curr = 1
        for i in range(length):
            # print("curr_num", sorted_num[i], curr)
            if i + 1 < length:
                # print("inside if")
                next_num = sorted_num[i + 1]
                curr_num = sorted_num[i]

                if curr_num + 1 == next_num:
                    # print("added", curr_num, next_num, curr)
                    curr += 1
                else:
                    # print("disconnected", curr_num, next_num, curr)
                    maxi = max(maxi, curr)
                    curr = 1

        maxi = max(maxi, curr)
        
        return maxi