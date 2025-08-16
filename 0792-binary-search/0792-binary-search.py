class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Time: O(log n)
        Space: O(1)

        The time complexity is O(log n) since half the search space is being eliminated after 
        each iteration. 
        
        [-3, 0, 2, 6, 9]
        """
        L = 0          # inclusive
        R = len(nums)  # exclusive
        while L < R:
            mid = (L + R) // 2
            if nums[mid] > target:  # we're too big
                R = mid             # make the nums smaller
            elif nums[mid] < target:  # we're too small
                L = mid + 1           # make the nums bigger
            else:
                return mid
        return -1
