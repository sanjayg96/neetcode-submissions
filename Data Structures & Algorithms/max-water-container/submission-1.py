class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        max_water = 0

        while l < r:
            w = r - l
            h = min(heights[l], heights[r])
            area = w * h

            if area > max_water:
                max_water = area

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return max_water
            