# https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_map = {}
        for ind, num in enumerate(nums):
            if num in complement_map:
                return [complement_map[num], ind]
            complement_map[target - num] = ind
