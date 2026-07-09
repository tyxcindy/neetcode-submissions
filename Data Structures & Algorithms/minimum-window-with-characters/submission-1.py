class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ## Base Cases
        if len(s) < len(t):
            return ""
        elif s == t:
            return s

        ## Calculating all letters needed
        t_counts = {}
        for letter in t:
            t_counts[letter] = t_counts.get(letter, 0) + 1

        t_set = set(t_counts.keys())

        ## Sliding Window
        min_res = float("inf")
        left_ptr = 0

        # Final Solution
        solution_found = False
        left_stop = 0
        right_stop = len(s) - 1
        
        for right_ptr in range(len(s)):
            right = s[right_ptr]

            if right in t_set:
                # Remove needed letters from s_count till s_count is empty
                t_counts[right] = t_counts.get(right, 0) - 1

            ## All letters are found (all values are 0)
            while max(t_counts.values()) <= 0:
                solution_found = True
                # Save ptrs when new minimum is reached
                if right_ptr - left_ptr + 1 < min_res:
                    min_res = right_ptr - left_ptr + 1
                    left_stop = left_ptr
                    right_stop = right_ptr + 1
                    
                # Shrink left till not possible
                left = s[left_ptr]
                if left in t_set:
                    t_counts[left] = t_counts.get(left, 0) + 1

                left_ptr += 1

        return s[left_stop:right_stop] if solution_found else ""