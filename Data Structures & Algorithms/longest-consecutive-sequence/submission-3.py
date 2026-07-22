class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)

        max_len = 0

        for i, n in enumerate(nums):
            if n-1 in set_nums:
                continue
            else:
                temp_len = 1
                consec_n = n
                while consec_n + 1 in set_nums:
                    consec_n += 1
                    temp_len += 1
                
                max_len = max(max_len, temp_len)

        return max_len