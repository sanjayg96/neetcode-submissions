class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[-1] > nums[0]:
            return nums[0]
        if len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums) - 1

        while l < r:
            if l + 1 == r:
                return min(nums[l], nums[r])
            m = (l + r) // 2
            if nums[r] < nums[m]:
                l = m
            else:
                r = m
