class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for i in nums:
            if i not in freq_dict:
                freq_dict[i] = 0
            freq_dict[i] += 1
        freq_dict = sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)[:k]
        top_k_values = [key for key, value in freq_dict]
        return top_k_values
        