import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        ### PROBLEM INFO ###
        * ith pile has `piles[i]` bananas
        * guards will come back in `h` hours
        * `k` is banana eating speed (banana per hour)
        * If k > piles[i], she eats the entire pile only. Not any from the next pile

        Obviously if `k` is very large, she can eat quickly within the allotted time.
        She likes taking her time and wants to eat the fewest bananas possible while
        still finishing before h.

        ### BRUTE FORCE ###
        From Ex. 2, we see that if len(piles) == h, then k is max(piles).
        This makes sense as Koko must each the most bananas as the biggest
        pile if she wants to finish in time.

        This means for a brute force solution, we can start at max(piles) and
        try every k in the range of [max(piles), 1] going down by 1 each time.
        We are guaranteed to find the optimal `k` then!
        """

        """
        Time: O(n^2)
        Space: O(1)

        smallest_banana_eating_speed = float('inf')
        for banana_eating_speed in range(max(piles), 0, -1):
            total_time_taken = 0
            for pile in piles:
                total_time_taken += math.ceil(pile / banana_eating_speed)
            
            if total_time_taken <= h:
                smallest_banana_eating_speed = min(smallest_banana_eating_speed, banana_eating_speed)
            else:
                break
        return smallest_banana_eating_speed
        """

        """
        ### NEW APPROACH ###
        Rather than iterating over the range [max(piles), 1] going down by 1,
        we can use binary search to find the optimal solution
        """
        L_banana_eating_speed = 1               # inclusive
        R_banana_eating_speed = max(piles) + 1  # exclusive
        smallest_banana_eating_speed = float("inf")
        while L_banana_eating_speed < R_banana_eating_speed:
            mid_banana_eating_speed = (L_banana_eating_speed + R_banana_eating_speed) // 2
            
            total_time_taken = 0
            for pile in piles:
                total_time_taken += math.ceil(pile / mid_banana_eating_speed)
            
            # We are taking too long
            # so we need to increase the banana eating speed
            if total_time_taken > h:
                L_banana_eating_speed = mid_banana_eating_speed + 1

            # We successfully finished the bananas within the time
            # but see if we can make the banana eating speed smaller
            else:
                smallest_banana_eating_speed = min(smallest_banana_eating_speed, mid_banana_eating_speed)
                R_banana_eating_speed = mid_banana_eating_speed

        return smallest_banana_eating_speed