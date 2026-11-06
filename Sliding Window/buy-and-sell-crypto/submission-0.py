class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        best=0

        for price in prices:
            min_price = min(min_price,price)
            profit= price-min_price

            best = max(profit,best)
        
        return best
