class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        unique_nums = set(nums)
        for num in unique_nums:
            # num is not the start of a consecutive sequence
            if num-1 in unique_nums:
                continue
            
            # num is the start of the sequence
            n = num
            curr_length = 1
            while n+1 in unique_nums:
                curr_length += 1
                n += 1
            max_length = max(max_length, curr_length)

        return max_length