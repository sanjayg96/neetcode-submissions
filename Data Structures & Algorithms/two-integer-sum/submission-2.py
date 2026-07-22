class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track = {}

        for i, n in enumerate(nums):
            complement = target - n
            if complement in track:
                index_1 = track[complement]
                index_2 = i
            else:
                track[n] = i

        return [index_1, index_2]