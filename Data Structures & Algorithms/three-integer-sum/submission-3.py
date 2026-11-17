class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        n=len(nums)
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            if nums[i] > 0:
                break

            target = -nums[i]
            j=i+1
            k=n-1
            while j<k:
                current_sum = nums[j]+nums[k]
                if current_sum > target:
                    k-=1
                elif current_sum < target:
                    j+=1
                else:
                    result.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1

                    while j<k and nums[j] == nums[j-1]:
                        j+=1
                    while j<k and nums[k] == nums[k+1]:
                        k-=1


        return result
        