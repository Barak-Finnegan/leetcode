# https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alphabet = 26 * [ 0 ]
        for ch in s:
            alphabet [ord(ch) - ord('a')] += 1
        for ch in t:
            alphabet [ord(ch) - ord('a')] -= 1
        for val in alphabet:
            if val != 0:
                return False
        return True
