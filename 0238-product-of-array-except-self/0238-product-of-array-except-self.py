class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Optimal: Use output array to store prefix products, then multiply suffix products
        in the output array itself
        Time: O(n)
        Space: O(1) since outpt array does not count
        """

        prefix_prod = 1  # cumulative prefix product
        ans = [None] * len(nums)
        for i in range(len(nums)):
            ans[i] = prefix_prod
            prefix_prod *= nums[i]

        # At this point, ans contains the prefix products.
        # It is just prefix_products with a different name

        suffix_prod = 1  # cumulative suffix product 
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= suffix_prod
            suffix_prod *= nums[i]
        return ans        

    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     """
    #     Suboptimal: Arrays for prefix and suffix products
    #     Time: O(n)
    #     Space: O(n) for the prefix and suffix sums
    #     """

    #     prefix_prod = 1  # cumulative prefix product
    #     prefix_products = [None] * len(nums)  # prefix_products[i] contains the product of elements 0 to i-1
    #     for i in range(len(nums)):
    #         prefix_products[i] = prefix_prod
    #         prefix_prod *= nums[i]

    #     suffix_prod = 1  # cumulative suffix product 
    #     suffix_products = [None] * len(nums)  # suffix_products[i] contains the product of elements i+1 to end
    #     for i in range(len(nums) - 1, -1, -1):
    #         suffix_products[i] = suffix_prod
    #         suffix_prod *= nums[i]
        
    #     ans = []
    #     for i in range(len(nums)):
    #         ans.append(prefix_products[i] * suffix_products[i])
    #     return ans


    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     """
    #     Brute Force: Nested loop to skip an index and compute product of rest of the list
    #     Time: O(n^2)
    #     Space: O(1) not counting output array
    #     """
    #     ans = [None] * len(nums)
    #     for skip_index in range(len(nums)):
    #         product = 1
    #         for i, num in enumerate(nums):
    #             if i == skip_index:
    #                 continue
    #             product *= num
    #         ans[skip_index] = product
    #     return ans