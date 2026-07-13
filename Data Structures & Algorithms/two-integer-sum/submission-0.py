class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track_map = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in track_map:
                return [track_map[diff], i]
            track_map[n] = i

        return None