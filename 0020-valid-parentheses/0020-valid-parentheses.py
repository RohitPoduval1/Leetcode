class Solution(object):
    def isValid(self, s):
        """
        Use a STACK! Why? → "Open brackets must be closed in the correct order" means a LIFO data
        structure is useful (AKA Stack).

        PUSH opening brackets on the stack
        When to pop? When we encounter closing brackets. The opening brackets on the stack should
        pair with the current closing bracket
        
        Time: O(n)
        Space: O(n)
        """
        stack = []
        closing_opening = {
            ')': '(',
            '}': '{',
            ']':'['
        }
        opening_brackets = ['(', '{', '[']
        for bracket in s:
            # Bracket is opening
            if bracket in opening_brackets:
                stack.append(bracket)  # push onto stack

            # Bracket is closing
            else:
                # if the opening bracket on the stack does not match
                # with the corresponding opening bracket to the current closing bracket,
                # the parentheses are not valid
                if len(stack) == 0:
                    return False

                corresponding_opening_bracket = closing_opening[bracket]
                if stack.pop() != corresponding_opening_bracket:
                    return False
        return len(stack) == 0