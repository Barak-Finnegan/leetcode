# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            t1, t2 = None, None
            if token in '*/+-':
                t1, t2 = int(stack.pop()), int(stack.pop())
            if token == '*':
                stack.append(t1 * t2)
            elif token == '/':
                stack.append(int(t2 / t1))
            elif token == '-':
                stack.append(t2 - t1)
            elif token == '+':
                stack.append(t1 + t2)
            else:
                stack.append(token)

        return int(stack[0])
