class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums = sorted(set(nums))
        # print("nums", nums)
        # max_len = 1 if nums else 0
        # tem_len = 1 if nums else 0
        # for i in range(1,len(nums)):
        #     if nums[i] == nums[i-1] + 1:
        #         tem_len += 1
        #         # print("tem_len", tem_len)
        #     else:
        #         if tem_len > max_len:
        #             max_len = tem_len
        #             # print("max_len", max_len)
        #         tem_len = 1
        # return max_len if max_len > tem_len else tem_len

        # better approach
        nums = set(nums)
        tol_len = 0
        for num in nums:
            if (num - 1) not in nums:
                cur_num = num
                cur_len = 1
                while (cur_num + 1) in nums:
                    cur_len += 1
                    cur_num += 1
                if cur_len > tol_len:
                    tol_len = cur_len
        return tol_len