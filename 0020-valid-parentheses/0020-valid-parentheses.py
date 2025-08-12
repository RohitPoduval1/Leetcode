class Solution(object):
    def isValid(self, s):
        """
        "Open brackets must be closed in the correct order."
        This means we should use a STACK!

        When do we push to the stack?
            When we see an opening bracket.
        When do we pop from the stack?
            When we see a closing bracket.
            The closing bracket that we are on MUST match the bracket
            popped from the stack. If it does not, then `s` is invalid.

        Time: O(n)
        Space: O(n)
        """
        opening_to_closing = {
            '(': ')',
            '[': ']',
            '{': '}',
        }
        opening_brackets = []
        for bracket in s:
            # Opening bracket
            # Push to stack
            if bracket in ('(', '[', '{'):
                opening_brackets.append(bracket)
                continue
            
            # Closing bracket
            # Pop opening bracket from stack if there are opening brackets even there
            if len(opening_brackets) == 0:
                return False

            opening_bracket = opening_brackets.pop()
            if opening_to_closing[opening_bracket] != bracket:
                return False

        return len(opening_brackets) == 0