class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        BRUTE FORCE: Nested for loop to find the bigger number for each number in the array
        Time: O(N²)
        Space: O(1)
    
    
        PUSH if the current temp is less than or equal to the top of the stack
        POP if the current temp is greater than the top of the stack (since temps can be resolved
        with that greater temp)

        OPTIMIZED: Stack (monotonic in decreasing order)
        Time: O(N)
        Space: O(N) with the stack (answer array does not count in space complexity)
        """

        answer = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            
            # while the current temp is able to resolve unresolved temps in the stack
            while stack and temp > stack[-1][0]:
                stack_temp, stack_index = stack.pop()
                answer[stack_index] = i - stack_index
            
            stack.append( (temp, i) )

        return answer