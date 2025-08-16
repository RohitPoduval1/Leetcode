class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Rotating an array 1 time means moving each number to the right by 1 position. Rotating an
        array k times means shifting over each number to the right k times (with wrap around)

        Looking at the testcase, we can notice a pattern of comparing the middle element to the
        rightmost element.
            • if nums[middle] > nums[right]: look in the right half
            • else (nums[middle] < nums[right]): look in the left half
            • don't need to worry about nums[middle] == nums[right] since "all the integers of nums
            are unique"
        """

        minn = float("inf")
        left = 0               # inclusive
        right = len(nums) - 1  # inclusive

        while left <= right:
            middle = (left + right) // 2
            minn = min(minn, nums[middle])
            if nums[middle] > nums[right]:
                left = middle + 1
            # else works since "all the integers of nums are unique"
            else:
                right = middle - 1

        return minn