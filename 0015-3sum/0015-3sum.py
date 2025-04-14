class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        for i, fixed_num in enumerate(nums):
            # not first element and matches the previous fixed number
            if i > 0 and fixed_num == nums[i-1]:
                continue  # we have already computed it so move on
            
            # SORTED TWO-SUM
            L = i + 1
            R = len(nums) - 1

            while L < R:
                summ = nums[L] + nums[R]
                # the target sum is the negative of fixed_num since summ + fixed_num
                # should be 0. It then follows that summ should be -fixed_num
                if summ > -fixed_num:     # we are too big
                    R -= 1
                elif summ < -fixed_num:   # we are too small
                    L += 1
                else:
                    triplets.append([fixed_num, nums[L], nums[R]])
                    # Increment the pointers (as per two pointers extreme)
                    L += 1
                    R -= 1

                    """
                    BUT, consider the case where a pointer, say L, moves to the same number
                    In this case, we are just computing the same values again, which we don't
                    want, so move L to a unique number.
                    """
                    # while nums[L] is the same value it just was
                    while nums[L] == nums[L-1] and L < R:
                        L += 1  # increment it to keep searching so it's not the same value
                    
                    # while nums[R] is the same value it just was
                    while nums[R] == nums[R+1] and L < R:  
                        R -= 1  # decrement it to keep searching so it's not the same value

        return triplets