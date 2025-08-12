class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        We need to track the state of the expression, evaluating sub-expressions
        in order (i.e., 2+1 before *3 in Ex. 1).
        This means we should use a STACK.

        When do we push to the stack?
            When we see an integer (not in the list of operators)
        When do we pop from the stack?
            When we see an operator (+, -, *, /)

        Time: O(n)
        Space: O(n)
        """
        if len(tokens) == 1:
            return int(tokens[0])

        nums_stack = []
        for token in tokens:
            ### Token is an integer ###
            if token not in ['+', '-', '*', '/']:
                nums_stack.append(int(token))
                continue
            
            ### Token is an operator ###
            # We are guaranteed that "The input represents a valid arithmetic
            # expression in a reverse polish notation" so we can pop 2x without worry
            num2 = nums_stack.pop()
            num1 = nums_stack.pop()

            match token:
                case '+':
                    subexpr_result = num1 + num2
                case '-':
                    subexpr_result = num1 - num2
                case '*':
                    subexpr_result = num1 * num2
                case '/':
                    # The division between two integers always truncates toward 0
                    # -1 / 2 = -0.5 becomes 0 NOT -1
                    subexpr_result = int(num1 / num2)

            nums_stack.append(subexpr_result)
            print(subexpr_result)

        return nums_stack[0]