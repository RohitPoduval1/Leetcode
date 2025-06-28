class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        **Understanding the Problem**
            Longest common PREFIX means...
            * Answer will not be letters found in the middle or end of the string
            * We can start our search at the beginning of the string
        """
        # It is possible that strs[i] could be an empty string ""
        if "" in strs:
            return ""

        # The answer can only be as long as the shortest string
        # since there is a case where the shortest string is the entire prefix
        ans = ""
        char_to_compare_index = 0
        shortest_string = self._get_shortest_string(strs)

        while char_to_compare_index < len(shortest_string):
            char_to_compare = shortest_string[char_to_compare_index]
            for i, string in enumerate(strs):
                if string[char_to_compare_index] != char_to_compare:
                    return ans
                
                # We are on the last string and all strings have matched so far
                if i == len(strs) - 1:
                    ans += string[char_to_compare_index]
            char_to_compare_index += 1
        
        return ans
    
    def _get_shortest_string(self, strs) -> str:
        shortest = ("", float("inf"))
        for string in strs:
            if len(string) < shortest[1]:
                shortest = (string, len(string))
        return shortest[0]