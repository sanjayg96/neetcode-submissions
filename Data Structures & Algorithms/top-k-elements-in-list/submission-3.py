from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums = {}

        for n in nums:
            count_nums[n] = count_nums.get(n, 0) + 1

        rank = [[] for _ in range(len(nums))]
        for n, c in count_nums.items():
            rank[c-1].append(n)

        

        final_result = []
        for i in range(len(nums) - 1, -1, -1):
            if rank[i]:
                final_result = final_result + rank[i]

            if len(final_result) == k:
                return final_result

        return None

