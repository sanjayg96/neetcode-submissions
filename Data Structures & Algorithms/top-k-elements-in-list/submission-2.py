from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {} # number: count
        for i, n in enumerate(nums):
            frequency[n] = frequency.get(n, 0) + 1

        buckets = [[] for _ in range(len(nums))]

        for n, c in frequency.items():
            buckets[c-1].append(n)

        final_result = []
        for i in range(-1, -1 * (len(nums) + 1), -1):
            final_result = final_result + buckets[i]

            if len(final_result) == k:
                return final_result

