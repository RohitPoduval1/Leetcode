from collections import defaultdict


class Solution:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     """
    #     Suboptimal: Track occurences of each num and sort by occurences
    #     Time: O(n logn)
    #     Space: O(n)
    #     """
    #     # Populate occurences hashmap
    #     num_occurences = defaultdict(int)
    #     for num in nums:
    #         num_occurences[num] += 1
        
    #     # Sort dict by values (occurences)
    #     sorted_occurences = dict(sorted(num_occurences.items(), key=lambda item: item[1], reverse=True))
        
    #     # Return top k frequent elements
    #     return list(sorted_occurences.keys())[:k]
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Optimal: Use array with index i as the count/numberOfOccurences and value as
        a list of elements that occur that many times
        Time: O(n logn)
        Space: O(n)
        """
        # Populate occurences hashmap
        num_occurences = defaultdict(int)
        for num in nums:
            num_occurences[num] += 1
        
        occurences = [None] * (len(nums) + 1)
        for num in num_occurences:
            if occurences[num_occurences[num]] is None:
                occurences[num_occurences[num]] = [num]
            else:
                occurences[num_occurences[num]].append(num)

        # At this point we have an array with the count as the index and the list of
        # numbers that occur i times at index i
        
        ans = []
        for i in range(len(occurences)-1, -1, -1):
            if occurences[i] is not None:  # there is a list of nums at index i
                # go through the list while we still need numbers 
                for num in occurences[i]:
                    if len(ans) < k:
                        ans.append(num)
                    else:
                        return ans

        return ans




        