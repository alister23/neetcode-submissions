class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest = 101
        profit = 0
        for price in prices:
            cheapest = min(cheapest, price)
            profit = max(price-cheapest, profit)

        return profit