from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Optimal: Hashmap to track occurences of each character.
        (If s and t are anagrams, then the same number of each character will be in each string)
        Time: O(n)
        Space: O(n)
        """

        # O(1) check. Not the same length means there are not anagrams
        if len(s) != len(t):
            return False

        # Populates each nonexistent entry with a default value (in this case 0) because int
        # was provided. Very useful because we don't have to check if the key exists.
        char_occur = defaultdict(int)
        for char in s:
            char_occur[char] += 1
        
        for char in t:
            char_occur[char] -= 1
        
        for char in char_occur:
            if char_occur[char] != 0:  # a character occured more times in either s or t
                return False           # meaning s and t are not anagrams
        
        return True
