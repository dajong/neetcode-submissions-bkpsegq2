class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxProfit = 0
        minPrices = prices[0]

        for r in range(1, len(prices)):
            minPrices = min(prices[r], minPrices)
            maxProfit = max(prices[r] - minPrices, maxProfit)

        return maxProfit
