class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()
        num_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [i, num_index[complement]]
            else:
                num_index[num] = i
                seen.add(num)

    """
    # Brute Force
    # Time: O(n)
    # Space: O(1)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
    """
            

        