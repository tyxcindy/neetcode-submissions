import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        translator = str.maketrans("", "", string.punctuation + " ")
        s = s.translate(translator)

        if s == s[::-1]:
            return True
        else:
            return False
