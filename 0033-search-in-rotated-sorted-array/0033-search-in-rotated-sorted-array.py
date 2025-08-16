class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        There are 2 possible array configurations after an array is rotated...
            1. The array is in ascending sorted order which occurs after the array is rotated
            effectively 0 times.
            2. The array is separated into a left and right part, both of which are sorted on their
            own but are not sorted together.
        
        How to handle these cases?
            1. If the array is already fully sorted, just do a binary search on the entire array 
            to find nums.
            2. If there are a left and right part, we need to find which part is target in and
            search in that part of the array.
        
        Handling Case 2:
            Notice that in Ex. 1 that 0 AKA min(nums), separates the 2 parts of the array. This
            means if we find min(nums), we have found where the 2 parts of nums are.
        
        Step 1: Find the index of min(nums) with Binary Search
        Step 2: Look in the correct part of the array based on index_of_min and target

        Time: O(log n)
        Space: O(1)
        """
        minn = float("inf")
        index_of_min = -1
        left = 0               # inclusive
        right = len(nums) - 1  # inclusive
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] < minn:
                minn = nums[middle]
                index_of_min = middle

            if nums[middle] == target:
                return middle
            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle - 1

        # left and right are both inclusive
        # the array is in sorted order with effectively 0 rotations
        if index_of_min == 0:
            left = 0
            right = len(nums) - 1
        # the target is in the left part of nums
        elif nums[0] <= target <= nums[index_of_min - 1]:
            left = 0
            right = index_of_min - 1
        # the target is in the right part of nums
        else:
            left = index_of_min
            right = len(nums) - 1
        
        # Binary Search on the correct part of the array
        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        
        return -1