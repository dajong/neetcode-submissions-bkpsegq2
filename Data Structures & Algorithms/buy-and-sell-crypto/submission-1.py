class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minPrice = prices[0]

        for i in range(1, len(prices)):
            res = max(prices[i] - minPrice, res)
            minPrice = min(minPrice, prices[i])
        return res   