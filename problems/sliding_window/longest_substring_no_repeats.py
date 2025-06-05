# https://leetcode.com/problems/longest-substring-without-repeating-characters/description

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        longest, origin, seen = 0, 0, {}
        for ind, ch in enumerate(s):
            if ch not in seen:
                seen[ch] = ind
                if ind - origin > longest:
                    longest = ind - origin
            else:
                tmp = seen[ch] + 1
                for removing in range(origin, tmp):
                    del seen[s[removing]]
                seen[ch] = ind
                origin = tmp

        return longest + 1
