class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_dict = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in seen_dict:
                index_1 = seen_dict[compliment]
                index_2 = i
            else:
                seen_dict[nums[i]] = i
        
        return [index_1, index_2]