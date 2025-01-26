from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_group = defaultdict(list)
        for s in strs:
            sorted_str = "".join(sorted(s))
            sorted_group[sorted_str].append(s)
        
        out = []
        for key in sorted_group:
            out.append(sorted_group[key])
        
        return out
    
