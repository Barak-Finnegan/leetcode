# https://leetcode.com/problems/encode-and-decode-strings/description/

class Solution:

    def encode(self, strs: List[str]) -> str:
        new_list = []
        for st in strs:
            new_list.append("||")
            new_list.append(st)
        return "".join(new_list[1:])

    def decode(self, s: str) -> List[str]:
        return s.split("||")
