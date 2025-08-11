class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Time: O(n1 + n2)
            n1 - len(s1)
            n2 - len(s2)
        Space:
            O(m + n)
            O(1) optimally using ASCII and array
        """
        if len(s1) > len(s2):
            return False
            
        # Hashmaps that hold the frequency of each letter
        s1_freq = defaultdict(int)
        s2_freq = defaultdict(int)
        for i in range(len(s1)):
            s1_freq[s1[i]] += 1  # populate s1 hashmap
            s2_freq[s2[i]] += 1  # build up the initial window
        
        # Cover the case where the current window of s2 is a permutation of s1
        if s1_freq == s2_freq:
            return True

        # Slide window over where we left off 
        for i in range(len(s1), len(s2)):
            s2_freq[s2[i]] += 1  # expanding the window

            # Contracting the window by removing characters that have exited the window
            left_char = s2[i - len(s1)]
            s2_freq[left_char] -= 1  

            # Since we are using defaultdict, a freq of 0 means the character should no longer
            # be in the hashmap since then it won't match up with s1 even if they are equal
            if s2_freq[left_char] == 0:
                del s2_freq[left_char]
            
            if s1_freq == s2_freq:
                return True
        
        return False
