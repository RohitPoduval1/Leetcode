from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Suboptimal: Track occurences of each num and sort by occurences
        Time: O(n logn)
        Space: O(n)
        """
        # Populate occurences hashmap
        num_occurences = defaultdict(int)
        for num in nums:
            num_occurences[num] += 1
        
        # Sort dict by values (occurences)
        sorted_occurences = dict(sorted(num_occurences.items(), key=lambda item: item[1], reverse=True))
        
        # Return top k frequent elements
        return list(sorted_occurences.keys())[:k]