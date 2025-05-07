# https://leetcode.com/problems/group-anagrams/description/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def to_tuple(word: str):
            alphabet = 26 * [ 0 ]
            for ch in word:
                alphabet[ord(ch) - ord('a')] += 1
            return tuple(alphabet)

        answers = {}
        for st in strs:
            tup = to_tuple(st)
            if tup in answers:
                answers[tup].append(st)
            else:
                answers[tup] = [ st ]

        return [ _ for _ in answers.values() ]
