class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        # Brute Force: Loop through all possible substrings with set to keep track of seen chars
        # Time: O(n^2)
        # Space: O(n)
        if len(s) == 0 or len(s) == 1:
            return len(s)

        max_length = 0
        for substr_start in range(len(s)):
            seen = set()
            seen.add(s[substr_start])
            for j in range(substr_start+1, len(s)):
                if s[j] not in seen:
                    seen.add(s[j])
                else:
                    max_length = max(max_length, len(seen))
                    break
        
        return max_length
        """

        # Optimized: Dynamic Sliding Window
        # What is a valid window? One without duplicate characters
            # Expand window if there are no duplicate chars
            # Contract window if there are duplicate chars in the window
        # A hashset is needed to keep track of seen chars
        if len(s) == 0 or len(s) == 1:
            return len(s)

        max_length = 0
        seen_chars = set()
        L = 0
        for R in range(len(s)):
            # Window is invalid, remove s[L] until it is valid
            while s[R] in seen_chars and L < len(s):
                seen_chars.remove(s[L])
                L += 1
            
            # Valid window now
            seen_chars.add(s[R])
            window_length = R - L + 1
            max_length = max(max_length, window_length)

        return max_length