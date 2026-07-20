class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_to_right_prod = []
        right_to_left_prod = []
        result = []

        temp_prod = 1
        for n in nums:
            temp_prod *= n
            left_to_right_prod.append(temp_prod)

        temp_prod = 1
        for n in nums[::-1]:
            temp_prod *= n
            right_to_left_prod.append(temp_prod)

        right_to_left_prod = right_to_left_prod[::-1]

        for i in range(len(nums)):
            left_index = i - 1
            right_index = i + 1

            left_prod = left_to_right_prod[left_index] if left_index >= 0 else 1
            right_prod = right_to_left_prod[right_index] if right_index < len(nums) else 1

            result.append(left_prod * right_prod)

        return result
