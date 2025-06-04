# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_ind, profit = 0, 0
        for ind, ele in enumerate(prices):
            if prices[min_ind] > ele:
                min_ind = ind

            if ele - prices[min_ind] > profit:
                profit = ele - prices[min_ind]

        return profit
