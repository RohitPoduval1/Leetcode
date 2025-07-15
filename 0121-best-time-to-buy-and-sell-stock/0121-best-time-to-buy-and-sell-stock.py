class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Brute Force: Nested for loop to see if we buy on day i and sell on day j, how much money can we make?
        Time: O(N^2)
        Space: O(1)

        Optimized: We know that time can only flow in 1 direction––forwards. Using this, we can keep track of
        the min price we have seen so far and use that to calculate profit.
        1. Calculate min_price
        2. Use that min_price to calculate max_profit seen so far
        Time: O(N)
        Space: O(1)
        """

        max_profit = 0
        min_price = prices[0]

        for price in prices:
            min_price = min(min_price, price)

            # profit = sell - buy (since sell > buy to actually make money)
            max_profit = max(max_profit, price - min_price)
        
        return max_profit