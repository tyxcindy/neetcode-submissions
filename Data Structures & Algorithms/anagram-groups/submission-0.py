class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_anagram = {}
        for anagram in strs:
            str_str = ''.join(sorted(anagram))
            sorted_anagram.setdefault(str_str, [])
            sorted_anagram[str_str].append(anagram)

        result = []

        for key, value in sorted_anagram.items():
            result.append(value)

        return result