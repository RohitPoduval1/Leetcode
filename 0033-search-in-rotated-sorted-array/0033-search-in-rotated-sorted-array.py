class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        * nums is sorted in ascending order (all with distinct values)
        * target may or MAY NOT be in nums (return -1 if its not there)
            otherwise return the index of target
        
        When you split the array down the pivot (where the nums switch) ascension,
        both halves will be sorted.

        There are 3 indices of interest:
            * 0: the start of the array
            * len(nums)-1: the end of the array
            * mindex: the index of the minimum in the array that splits the
                array into 2 sorted halves
        """
        L = 0
        R = len(nums)-1
        while L < R:
            mid = (L + R) // 2
            if nums[mid] > nums[R]:
                L = mid + 1
            else:
                R = mid

        ### Binary Search in Sorted Part ###
        mindex = L
        if target < nums[mindex]:
            return -1
        if target == nums[mindex]:
            return mindex
        if nums[mindex] < target <= nums[-1]:
            L = mindex + 1
            R = len(nums)
        else:
            L = 0
            R = mindex

        while L < R:
            mid = (L + R) // 2
            if nums[mid] < target:    # we are too small
                L = mid + 1           # make it bigger
            elif nums[mid] > target:  # we are too big
                R = mid               # make it smaller
            else:
                return mid
        
        return -1