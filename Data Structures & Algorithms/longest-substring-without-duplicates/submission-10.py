class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # char_set=[]
        # if len(s)==1:
        #     return 1
        # elif len(s) == 0:
        #     return 0
        # else:
        #     max_len=0
        #     curr_len=0
        #     for i in s:
        #         if i in char_set:
        #             curr_len=len(char_set)
        #             char_index=char_set.index(i)
        #             char_set=char_set[char_index+1:curr_len]
        #             char_set.append(i)
        #         else:
        #             char_set.append(i)
        #             curr_len=len(char_set)
        #         if curr_len > max_len:
        #                 max_len = curr_len
        #     return max_len


        # better approach
        last_seen = {}
        left = 0
        max_len = 0

        for curr_index, value in enumerate(s):
            if value in last_seen and last_seen[value] >= left:
                left = last_seen[value] + 1
            last_seen[value]=curr_index
            max_len=max(max_len,curr_index-left+1)
        return max_len