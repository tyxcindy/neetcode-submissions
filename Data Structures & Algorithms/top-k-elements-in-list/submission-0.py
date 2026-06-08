class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for num in nums:
            freq_dict.setdefault(num, 0)
            freq_dict[num] += 1
        
        def find_value(freq_dict, max_freq):
            for key, value in freq_dict.items():
                if value == max_freq:
                    return key

        result = [0] * k
        for i in range(k):
            max_freq = max(freq_dict.values())
            max_key = find_value(freq_dict, max_freq)
            result[i] = max_key
            del freq_dict[max_key]
        
        return result