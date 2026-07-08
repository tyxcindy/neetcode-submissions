class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        char_counts = {}
        max_res = 0
        left_ptr = 0
        most_ltr = 0

        for right_ptr in range(len(s)):
            right = s[right_ptr]

            char_counts[right] = char_counts.get(right, 0) + 1

            most_ltr = max(most_ltr, char_counts[right])
            
            if (right_ptr - left_ptr + 1) - most_ltr > k:
                char_counts[s[left_ptr]] -= 1
                left_ptr += 1
            
            max_res = max(right_ptr - left_ptr + 1, max_res)

        return max_res