from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        If s and t are anagrams, then the same number of each character will be in each string.
        We can run an initial check for length (which is a constant time operation) since if
        s and t have different length, we know they are not anagrams. Otherwise, use a hashmap
        and keep track of each character's occurences. If we run through s and t and each 
        character has an occurence of 0 by the end, we have an anagram. If it is not 0, then
        somewhere, t had a character that s did not, meaning they are not anagrams.
            Time: O(n)
            Space: O(n)
        """
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
            if char_occur[char] != 0:
                return False
        
        return True
