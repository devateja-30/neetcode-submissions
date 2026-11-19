class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # suffix_array=[]
        # max_profit=0
        # for i in range(0,len(prices)-1):
        #     if i==len(prices)-1:
        #         suffix_array.append(0)
        #     suffix_array.append(max(prices[i+1:len(prices)]))
        
        # for i in range(0,len(prices)-1):
        #     profit=suffix_array[i]-prices[i]
        #     if profit > max_profit:
        #         max_profit = profit
        # return max_profit
        left=prices[0]
        right=prices[0]
        max_profit=0
        for i in range(1,len(prices)):
            print("i",i)
            print("left",left)
            print("right",right)
            if prices[i] < left:
                left=prices[i]
                right=prices[i]

            if prices[i] > right:
                right=prices[i]
            
            profit=right-left
            print("left",left)
            print("right",right)
            print("profit",profit)
            if profit>max_profit:
                max_profit=profit
        return max_profit