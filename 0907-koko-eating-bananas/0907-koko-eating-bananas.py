class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        • Koko can eat at most 1 pile per hour. This is why they give the constraint of
        len(piles) ≤ h since if h < len(piles), its not possible to finish all bananas. 
        • hours spent eating bananas at piles[i] = ceil(piles[i] / k)

        BRUTE FORCE:
        Try all numbers from 1 to max(piles) inclusive and see which is the lowest number
        that eats all the bananas in the proper amount of hours. 
        • Time: O(n * m)
            n is len(piles)
            m is max(piles)
        • Space: O(1)

        OPTIMIZED: Literally optimize the brute force solution
        Instead of linearly walking through [1, max(piles)], use binary search on that array using
        more informed decisions. Those more informed decision are...
            • If you find a k that works, go smaller to see if you can do better
            • If you can't, make k bigger to get a working
        • Time: O(n * log(m))
        • Space: O(1)
        """
        smallest_k = float("inf")

        # the range of possible k values from [1, 2, 3, ..., max(piles)]
        left = 1            # inclusive
        right = max(piles)  # inclusive
        while left <= right:
            middle = (left + right) // 2  # the k we are looking at in the range of possible k values
            curr_hours = 0

            # Get how many hours it takes to finish the bananas with the current k
            for pile in piles:
                curr_hours += ceil(pile / middle)

            if curr_hours == h or curr_hours < h:
                smallest_k = min(smallest_k, middle)
                right = middle - 1  # see if you can do better if curr_hours == h
                                    # reduce k if the bananas were finished too quick
            
            # the bananas were eaten too slow
            else:
                left = middle + 1  # so increase k
            
        return smallest_k