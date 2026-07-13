import numpy as np

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            if i == len(nums) - 1:
                temp_list = nums[0:i]
            else:
                temp_list = nums[0:i] + nums[i+1:]
            res.append(int(np.prod(temp_list)))

        return res

        