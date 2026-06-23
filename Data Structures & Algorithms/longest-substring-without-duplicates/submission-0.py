class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        visited = set()

        str_len = len(s)

        curr_length = 0

        left = 0
        right = 0

        while right < str_len:
            left_ltr = s[left]
            right_ltr = s[right]
            if right_ltr in visited:
                max_length = curr_length if curr_length > max_length else max_length
                curr_length -= 1
                visited.remove(left_ltr)
                left += 1
            else:
                right += 1
                curr_length += 1
                visited.add(right_ltr)
        
        max_length = curr_length if curr_length > max_length else max_length

        return max_length