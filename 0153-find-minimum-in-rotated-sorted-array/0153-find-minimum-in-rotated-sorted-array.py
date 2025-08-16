class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        - `nums` is sorted in ascending order
        - `nums` may be rotated between [1, n] times
        - Rotating wraps elements around to the beginning

        ### WHY BINARY SEARCH ###
        We know that nums after the rotations still has some sort of sorted order
        and it started off sorted. This is a hint to use BINARY SEARCH.
        """
        L = 0              # inclusive
        R = len(nums) - 1  # inclusive

        while L < R:
            mid = (L + R) // 2

            # [3,4,5,1,2]
            # Ex. 1 -> nums[mid]=5   nums[R]=2
            if nums[mid] > nums[R]:
                # Pivot in the right half of nums, but WHY?
                # nums is sorted in ascending order. This means if
                # nums[mid] > nums[R], there must be some numbers in between those.
                # Those numbers contain the min.
                L = mid + 1
            
            # Ex. 2 -> nums[L]=7    nums[mid]=13
            else:
                # Pivot is either nums[mid] or in the left half of nums
                # [7, 9, 1, 4, 5]
                R = mid

        return nums[L]