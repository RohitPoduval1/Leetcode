class Solution:
    # Optimized
    # Time: O(n)
    # Space: O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        The whole algorithm revolves around complements. Loop through nums. Use a hashmap to
        store the current number and its index. If we find the complement in the hashmap,
        then we have our solution. A key distinction to make is adding to the hashmap only
        AFTER we check if the complement is in the hashmap. This is done to prevent the use
        of the same number in adding up to the target.
        """
        num_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_index:  # this is actually an O(1) operation!
                return [i, num_index[complement]]
            else:
                num_index[num] = i

    """
    Brute Force
    Time: O(n)
    Space: O(1)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
    """
            

        