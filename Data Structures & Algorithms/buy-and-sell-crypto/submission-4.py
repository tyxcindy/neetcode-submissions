class Solution:
    def maxProfit(self, prices: List[int]) -> int:        
        lowest_price = prices[0]
        max_price = 0

        for price in prices:
            if price < lowest_price:
                lowest_price = price
            else:
                price_diff = price - lowest_price
                if price_diff > max_price:  
                    max_price = price_diff

        return max_price

        