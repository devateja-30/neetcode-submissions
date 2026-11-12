class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(sorted(set(nums)))
        # print("nums", nums)
        max_len = 1 if nums else 0
        tem_len = 1 if nums else 0
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] + 1:
                tem_len += 1
                # print("tem_len", tem_len)
            else:
                if tem_len > max_len:
                    max_len = tem_len
                    # print("max_len", max_len)
                tem_len = 1
        return max_len if max_len > tem_len else tem_len