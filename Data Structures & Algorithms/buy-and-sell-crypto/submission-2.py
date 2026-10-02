class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left = -1
        for right, val in enumerate(prices):
            if right == 0:
                left += 1
                continue
            temp_profit = prices[right] - prices[left]

            
            if temp_profit > profit:
                profit = temp_profit
                print(left, right)

            if prices[right] < prices[left]:
                left = right
            

        return profit


            
