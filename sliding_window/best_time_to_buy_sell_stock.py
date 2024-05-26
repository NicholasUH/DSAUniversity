'''
Problem:
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''

'''
Logic:
create a left and right pointer
-left is used to indicate the lowest value to buy
-right is used to indicate the future highest value to sell
Iterate the right pointer to the end
-if left < right, see if new maximum
-if right < left, update left to new minimum
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right, max_profit = 0, 1, 0

        while right < len(prices):
            if prices[left] < prices[right]:
                max_profit = max(max_profit, prices[right] - prices[left])
            elif prices[left] > prices[right]:
                left = right
            
            right += 1
        
        return max_profit