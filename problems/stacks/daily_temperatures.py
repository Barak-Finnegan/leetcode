# https://leetcode.com/problems/daily-temperatures/description/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        height_stack = []
        answer = []
        for ind in range(len(temperatures) - 1, -1, -1):
            if not height_stack:
                height_stack.append((temperatures[ind], ind))
                answer.append(0)
                continue
            
            while temperatures[ind] >= height_stack[-1][0]:
                height_stack.pop()
                if not height_stack:
                    break

            if height_stack:
                answer.append(height_stack[-1][1] - ind)
            else:
                answer.append(0)
            height_stack.append((temperatures[ind], ind))

        return answer[::-1]
