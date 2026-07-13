import numpy as np

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]

        temp_prod_prefix = 1
        temp_prod_suffix = 1
        for i in range(len(nums) - 1):
            temp_prod_prefix *= nums[i]
            prefix.append(temp_prod_prefix)
        
        for i in range(len(nums) - 1, 0, -1):
            temp_prod_suffix *= nums[i]
            suffix.append(temp_prod_suffix)

        res = []
        for i in range(len(nums)):
            res.append(int(prefix[i] * suffix[-1 * (i + 1)]))
        

        return res

        