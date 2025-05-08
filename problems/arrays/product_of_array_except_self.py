# https://leetcode.com/problems/product-of-array-except-self/description/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sub_array_len = (len(nums) - 1)
        right_mult = sub_array_len * [ 1 ]
        left_mult = sub_array_len * [ 1 ]
        for ind in range(sub_array_len):
            if ind == 0:
                right_mult[-1], left_mult[0] = nums[-1], nums[0]
                continue
            right_mult[sub_array_len - ind - 1] = right_mult[sub_array_len - ind] * nums[sub_array_len - ind]
            left_mult[ind] = left_mult[ind - 1] * nums[ind]

        solution = [right_mult[0]]
        for ind in range(sub_array_len - 1):
            solution.append(left_mult[ind] * right_mult[ind + 1])
        solution.append(left_mult[-1])

        return solution
