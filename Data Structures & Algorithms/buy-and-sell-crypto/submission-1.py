class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_buy = 101
        best_profit = 0
        for price in prices:
            best_buy = min(best_buy, price)
            best_profit = max(best_profit, price-best_buy)
        return best_profit