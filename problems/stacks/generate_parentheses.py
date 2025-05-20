# https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answers = []
        def generateParenthesis(open, close, string):
            if open == close and open == n:
                return
            if open == n:
                answers.append(string + ")" * (open - close))
                return
            if open == close:
                generateParenthesis(open + 1, close, string + "(")
                return
            generateParenthesis(open, close + 1, string + ")")
            generateParenthesis(open + 1, close, string + "(")
            

        generateParenthesis(1,0,"(")
        return answers
