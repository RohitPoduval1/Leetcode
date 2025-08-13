class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        Problem Information:
            i (index): position in space
            abs(asteroid): size
            sign(asteroid): direction
                + right
                - left
            Asteroids move at same speed

            What happens if 2 meet?
                * Different size? -> Smaller explodes
                * Same size? -> Both explode
        
        Approach:
            We need to maintain a timeline/context so we use a STACK
            * When do we push? --> When we see a positive asteroid
            * When do we pop? --> Pop 2 asteroids and push asteroid based on collision logic

        * We only care whether about a negative asteroid if it is on top of a
        positive asteroid. Otherwise, just ignore it.

        Time: O(n): Despite nested while, an element is  never processed more
            than 2 times, leading to O(2n) or O(n) time complexity.
        Space: O(n): In the worst case, all elements may end up on the stack.
        """
        stack = []
        for asteroid in asteroids:
            if len(stack) == 0:
                stack.append(asteroid)
                continue

            ### NO COLLISION POSSIBLE ###
            if not self.is_collision_possible(curr_asteroid=stack[-1], incoming_asteroid=asteroid):
                stack.append(asteroid)
                continue

            ### COLLISION POSSIBLE, COMPARE ###
            # Current: --> (+) and Incoming: <-- (-) only remaining case
            while (
                (len(stack) > 0) and
                self.is_collision_possible(curr_asteroid=stack[-1], incoming_asteroid=asteroid) and
                (abs(asteroid) >= abs(stack[-1]))
            ):
                popped = stack.pop()
                # If they're equal size, both explode - don't add the incoming asteroid
                if abs(asteroid) == abs(popped):
                    asteroid = None  # Mark as destroyed
                    break
            
            # Add the surviving asteroid (if any) to the stack
            if asteroid is not None:
                if len(stack) == 0:
                    stack.append(asteroid)
                
                elif not self.is_collision_possible(curr_asteroid=stack[-1], incoming_asteroid=asteroid):
                    stack.append(asteroid)

        return stack
    

    def is_collision_possible(self, curr_asteroid: int, incoming_asteroid: int) -> bool:
        return not (
            (curr_asteroid > 0 and incoming_asteroid > 0) or  # Current: --> and Incoming: -->
            (curr_asteroid < 0 and incoming_asteroid < 0) or  # Current: <-- and Incoming: <--
            (curr_asteroid < 0 and incoming_asteroid > 0)     # Current: <-- and Incoming: --> 
        )