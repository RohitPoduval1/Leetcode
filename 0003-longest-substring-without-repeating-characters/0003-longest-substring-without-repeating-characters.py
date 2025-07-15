class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Brute Force: check all possible substrings with a nested for loop, keeping track
        of the longest one.
        Time: O(N^2)
        Space: O(1)

        Optimized: Dynamic-Sized Sliding Window

        while window is valid: expand it by adding more characters at R
        while window is invalid: contract it by removing characters at L
        A window is valid if there are no repeating characters present

        Time: O(N)
        Space: O(N)
        """

        unique_chars = set()  # for O(1) existence of characters
        longest = 0  # the longest substring seen

        left = 0
        for right in range(len(s)):
            # while the window is invalid
            while s[right] in unique_chars:
                unique_chars.remove(s[left])
                left += 1

            # The window is valid now
            unique_chars.add(s[right])
            # the longest between the longest we've seen and the current window length
            longest = max(longest, (right - left) + 1)

        return longest
