from collections import defaultdict


class Solution:
    # Time: O(n mlog(m)) where n is the length of strs and m is the length of the longest string
    # in strs
    # Space: O(n) since all strings will go in the hashmap by the end of the algorithm
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_group = defaultdict(list)
        for s in strs:
            sorted_str = "".join(sorted(s))
            sorted_group[sorted_str].append(s)
        
        out = []
        for key in sorted_group:
            out.append(sorted_group[key])
        
        return out