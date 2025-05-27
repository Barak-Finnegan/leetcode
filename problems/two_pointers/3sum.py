# https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        flag = False
        for ele in nums:
            if ele != 0:
                flag = True

        if not flag:
            return [[0, 0, 0]]
        solutions = set()
        for i in range(len(nums) - 1):
            complements, target = set(), -nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] in complements:
                    temp = [-target, nums[j], target - nums[j]]
                    solutions.add(tuple(sorted(temp)))
                else:
                    complements.add(target - nums[j])

        return [list(ele) for ele in solutions]
