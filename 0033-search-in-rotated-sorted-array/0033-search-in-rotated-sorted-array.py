class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        * nums is sorted in ascending order (all with distinct values)
        * target may or MAY NOT be in nums (return -1 if its not there)
            otherwise return the index of target
        """
        L = 0
        R = len(nums)-1

        while L <= R:
            mid = (L + R) // 2
            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[L] <= nums[mid]:
                # target is in the left half
                if nums[L] <= target < nums[mid]:
                    R = mid - 1
                # target is in the right half
                else:
                    L = mid + 1
            
            # Right half is sorted
            else:
                # target is in the left half
                if nums[mid] < target <= nums[R]:
                    L = mid + 1
                # target is in the right half
                else:
                    R = mid - 1

        return -1