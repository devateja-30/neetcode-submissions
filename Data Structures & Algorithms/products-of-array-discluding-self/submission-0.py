class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_array=[1 for i in range(len(nums))]
        suffix_array=[1 for i in range(len(nums))]
        final_array=[]
        for i in range(0,len(nums)):
            if i==0:
                continue
            prefix_array[i] = prefix_array[i-1] * nums[i-1]
        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:
                continue
            suffix_array[i]=suffix_array[i+1] * nums[i+1]
        for i in range(0,len(nums)):
            final_array.append(prefix_array[i]*suffix_array[i])
        return final_array
        