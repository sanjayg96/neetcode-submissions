class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # temp, ind

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                st_temp, st_ind = stack.pop()
                res[st_ind] = i - st_ind
            stack.append([t, i])

        return res