class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        n=len(numbers)-1
        while i<n:
            current_sum = numbers[i]+numbers[n]
            if current_sum > target:
                n-=1
            elif current_sum < target:
                i+=1
            else:
                return [i+1,n+1]
