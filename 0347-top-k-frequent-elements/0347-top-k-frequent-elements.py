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

    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     """
    #     Optimal: Use array with index i as the count/numberOfOccurences and value as
    #     a list of elements that occur that many times
    #     Time: O(n)
    #     Space: O(n)
    #     """
    #     # Populate occurences hashmap
    #     # the num itself mapped to how many times it appears
    #     num_occurences = defaultdict(int)
    #     for num in nums:
    #         num_occurences[num] += 1
        
    #     # An array where...
    #         # index: number of occurences
    #         # value: a list of the numbers that appear i times
    #     occurences = [None] * (len(nums) + 1)  # create list initialized with None
    #     for num in num_occurences:
    #         if occurences[num_occurences[num]] is None:  # no number has appeared that many times
    #             occurences[num_occurences[num]] = [num]
    #         else:
    #             occurences[num_occurences[num]].append(num)  # add to the existing list

    #     # At this point we have an array with the count as the index and the list of
    #     # numbers that occur i times at index i
    #     ans = []
    #     for i in range(len(occurences)-1, -1, -1):
    #         if occurences[i] is not None:  # there is a list of nums at index i
    #             # go through the list while we still need numbers
    #             for num in occurences[i]:
    #                 if len(ans) < k:
    #                     ans.append(num)
    #                 else:
    #                     return ans

    #     return ans

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Populate elem_occur
        # maps an element to the number of times it occurs in nums
        elem_freq = defaultdict(int)
        for num in nums:
            elem_freq[num] += 1

        # despite being an array, it cleverly maps the number of times an element occurs
        # to the elements that occur that many times
        freq_elem = [None] * (len(nums) + 1)  # a list of lists

        # Populating the frequency array
        for num, frequency in elem_freq.items():
            if freq_elem[frequency] is None:
                freq_elem[frequency] = [num]  # list does not exist yet, so create one
            else:
                freq_elem[frequency].append(num)  # already exists, just append to it
        
        top_k_frequent_elements = []
        # Loop through freq_elem in reverse order to get top k most frequent
        for i in range(len(freq_elem) - 1, -1, -1):
            elements_with_that_frequency = freq_elem[i]
            if elements_with_that_frequency is None:
                continue
            
            # There are elements with that frequency
            for element_with_that_frequency in elements_with_that_frequency:
                top_k_frequent_elements.append(element_with_that_frequency)
                if len(top_k_frequent_elements) == k:
                    return top_k_frequent_elements