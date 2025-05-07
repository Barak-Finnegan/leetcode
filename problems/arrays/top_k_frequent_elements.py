# https://leetcode.com/problems/top-k-frequent-elements/description/

from bisect import insort

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1
        sort = []
        for key, val in counter.items():
            insort(sort, [val, key])
        sort = sort[::-1]
        return [sort[i][1] for i in range(0, k)]
