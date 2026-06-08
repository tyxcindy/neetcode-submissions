class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters = {}
        for s_ltr in s:
            letters.setdefault(s_ltr, 0)
            letters[s_ltr] += 1
        
        for t_ltr in t:
            exist = letters.get(t_ltr)
            
            if not exist or exist == 0:
                return False

            letters[t_ltr] -= 1
        
        return True