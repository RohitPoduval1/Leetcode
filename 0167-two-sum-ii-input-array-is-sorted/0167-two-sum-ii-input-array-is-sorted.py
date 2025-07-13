class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        # Brute Force: Check every possible sum combination to see
        # if any lead to the target sum
        # Time: O(n^2)
        # Space: O(1)
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return (i+1, j+1)
        return (-1, -1)
        """

        # Opposite Ends Pointers
        # The fact that numbers is sorted means that...
            # incrementing the L pointer yields a larger sum
            # decrementing the R pointer yields a smaller sum
        # Time: O(n)  -> Pointers either break early or meet in middle, never crossing
        # Space: O(1) -> Only 2 integer variables regardless of length of numbers
        L = 0
        R = len(numbers) - 1

        while L < R:
            curr_sum = numbers[L] + numbers[R]
            if curr_sum == target:
                return (L+1, R+1)
            if curr_sum < target:
                L += 1
                continue
            if curr_sum > target:
                R -= 1
        return (-1, -1)  # should not happen