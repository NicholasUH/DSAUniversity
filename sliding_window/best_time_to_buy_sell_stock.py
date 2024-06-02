'''
Problem:
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''

'''
Logic:
To find the maximum profit we can use the sliding window technique. This helps make sure that we consider all possible combinations. We will
create two pointers, one starts at index 0 and another on index 1. We will iterate the right pointer to the end, and check if the right pointer
value is greater or less than the left pointer value. We say that the left pointer value is the buy day while the right is the sell day. If the 
current right pointer value is greater than the left, then we update the max profit, else we can assume that the right pointer is less than
the left, meaning we found a new lowest buy date so a greater max profit is possible.
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