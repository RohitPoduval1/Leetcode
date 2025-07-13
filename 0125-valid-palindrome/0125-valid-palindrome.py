class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        ### Converting the given palindrome check to code ###
        # Time: O(n)
        # Space: O(n), space needed for new string

        # 1. Standardize string to lowercase
        s = s.lower().strip()

        # 2. Remove all non alphanumeric characters
        new_s = ""
        for char in s:
            if char.isalnum():
                new_s += char
        
        # 3. Does the string read the same forwards and backwards?
        return new_s == new_s[::-1]
        """

        # Two pointers extreme: One at left end (L), one at right end (R)
        L = 0
        R = len(s) - 1
        while L < R:
            # Move pointers to valid alpha-numeric characters
            while not s[L].isalnum() and L < R:
                L += 1
            while not s[R].isalnum() and R > L:
                R -= 1
            
            # Now that both pointers are at valid chars, compare the chars
            if s[L].lower() != s[R].lower():
                return False  # not equal means the string is not a palindrome
            
            # Move pointers closer to progress
            L += 1
            R -= 1
        
        return True