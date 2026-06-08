class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupes = {}

        for num in nums:
            exist = dupes.get(num)

            if exist:
                return True
            
            dupes[num] = True

        return False