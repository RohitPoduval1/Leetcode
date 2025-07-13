class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        # We know we will have 2 heights, a left container height and a right container height
        # Height of container is min(height[L], height[R])
        # Width of container is R - L
        # Brute Force: Try every height combination and return the biggest area
        # Time: O(n^2)
        # Space: O(1)
        max_container_area = -1
        for L in range(len(height)):
            for R in range(L+1, len(height)):
                container_height = min(height[L], height[R])
                container_width = R - L
                container_area = container_width * container_height
                max_container_area = max(max_container_area, container_area)
        return max_container_area
        """

        max_container_area = -1
        L = 0
        R = len(height) - 1
        while L < R:
            container_height = min(height[L], height[R])
            container_width = R - L
            container_area = container_width * container_height
            max_container_area = max(max_container_area, container_area)
            if height[L] < height[R]:
                L += 1
            elif height[R] < height[L]:
                R -= 1
            else:
                L += 1
                R -= 1
        return max_container_area