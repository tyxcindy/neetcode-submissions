class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        output = []
        length = len(candidates)

        def dp(index, curr_combo, total):
            if total == target:
                output.append(curr_combo.copy())
                return
            
            if index >= length or total > target:
                return

            # Two Paths
            ## Include current candidates
            curr_combo.append(candidates[index])
            dp(index, curr_combo, total + candidates[index])
            ## Don't include current candidates
            curr_combo.pop()
            dp(index + 1, curr_combo, total)

            return

        dp(0, [], 0)
        
        return output
            