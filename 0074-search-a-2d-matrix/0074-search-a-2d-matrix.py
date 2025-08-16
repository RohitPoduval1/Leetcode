class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        1. Use binary search to find the list in matrix we have to search in
            Time: O(log m)
        2. Use binary search on that sublist to return whether target is in matrix
            Time: O(log n)

        Time: O(log(m * n)) = O(log m) + O(log n)
        Space: O(1)
        """
        left_sublist_index = 0
        right_sublist_index = len(matrix)
        MIDDLE_OF_SUBLIST = len(matrix[0]) // 2  # all sublists in matrix have the same length

        # Binary Search to find the list in the matrix that contains the target if it exists
        while left_sublist_index < right_sublist_index:
            middle_sublist_index = (left_sublist_index + right_sublist_index) // 2
            middle_sublist = matrix[middle_sublist_index]
            if middle_sublist[MIDDLE_OF_SUBLIST] == target:
                return True

            # the target will be in the sublist that has the proper range of numbers
            # use Binary Search in that sublist to see if the target is actually there
            if middle_sublist[0] <= target <= middle_sublist[-1]:
                return self.binarySearch(middle_sublist, target)

            # THE TARGET IS NOT IN THE CURRENT SUBLIST
            if middle_sublist[MIDDLE_OF_SUBLIST] > target:  # all numbers in the current sublist are too big
                right_sublist_index = middle_sublist_index
            else:  # all numbers in the current sublist are too small
                left_sublist_index = middle_sublist_index + 1

        return False


    def binarySearch(self, nums: List[int], target: int) -> bool:
        left = 0           # inclusive
        right = len(nums)  # exclusive

        while left < right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return True
            if nums[middle] > target:  # we need to get smaller
                right = middle
            else:                      # we need to get bigger
                left = middle + 1

        return False