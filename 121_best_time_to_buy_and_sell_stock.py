class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min = float ("inf")

        for price in prices:
            if price < min:
                min = price
                
            if price - min > profit:
                profit = price - min

        return profit