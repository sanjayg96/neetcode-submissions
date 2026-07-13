class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        set_nums = set(nums)

        max_len_list = []

        for n in nums:
            track_len = 1
            i = 1
            while (n + i) in set_nums:
                track_len += 1
                i += 1
            max_len_list.append(track_len)

        result = max(max_len_list)
        return result