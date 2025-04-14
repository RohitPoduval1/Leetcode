class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Time: O(n)
        Space: O(1)
        """
        L = 0
        R = len(numbers) - 1
        while L < R:
            summ = numbers[L] + numbers[R]
            
            # the sum is too big, make it smaller
            if summ > target:
                R -= 1

            # the sum is too small, make it bigger
            elif summ < target:
                L += 1
            
            # found the two numbers for the sum, return the indices (1-based)
            else:
                return [L+1, R+1]
        
        # not found
        return [-1, -1]
        