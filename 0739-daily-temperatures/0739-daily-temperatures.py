class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        We need to maintain a context/timeline of temperatures
            This is a hint that we need to use a stack.
        The giveaway for the data structure to use is "the number of days you have
        to wait after the ith day to get a warmer temperature"
            This is a dead giveaway that we need a MONOTONIC STACK.

        Should the stack be monotonically increasing or decreasing?
            We want the NEXT GREATER element -> monotonically decreasing stack
        
        Time: O(n) - Despite while nested in the for, we are only processing n elements.
            An element is either in the list or in the stack. Since we don't
            process elements multiple times, it is linear time complexity.
        Space: O(n) - In the worst case, all elements are added to the stack (Ex. 2 and 3)
        """
        ans = [0] * len(temperatures)
        md_stack = []  # a monotonically decreasing stack
        for i in range(len(temperatures)-1, -1, -1):
            curr_temp = temperatures[i]

            while len(md_stack) > 0 and curr_temp >= temperatures[md_stack[-1]]:  # recall we store indexes rather than actual temps
                md_stack.pop()
            
            ### At this point, the element is poised to be pushed to the stack ###
            # There is nothing in the stack so just add the index (and element by definition)
            if len(md_stack) == 0:
                md_stack.append(i)
                # We would set `ans[i] = 0` but we already initialized to all 0s
                continue
            
            # There are elements in the stack but we want to push the element since its ready
            ans[i] = md_stack[-1] - i
            md_stack.append(i)

        return ans