# https://leetcode.com/problems/longest-consecutive-sequence/description/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        answer = 0
        for num in unique_nums:
            if (num - 1) not in unique_nums:
                chain_length = 1
                while (num + chain_length) in unique_nums:
                    chain_length += 1
                if chain_length > answer:
                    answer = chain_length
        return answer
