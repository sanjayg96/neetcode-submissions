class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        topk = [[] for i in range(len(nums)+1)]

        for number in nums:
            counter[number] = 1 + counter.get(number, 0)
            
        for number, count in counter.items():
            topk[count].append(number)

        res = []
        for i in range(len(topk) - 1, 0, -1):
            for j in topk[i]:
                res.append(j)
                if len(res) == k:
                    return res


            