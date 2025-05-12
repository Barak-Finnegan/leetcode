# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {'{' : '}', '[': ']', '(' : ')'}
        for ch in s:
            if ch in mapping:
                stack.append(ch)
            else:
                # s consists of parentheses only '()[]{}'
                if not stack:
                    return False
                if mapping[stack.pop()] != ch:
                    return False 
        return not stack
