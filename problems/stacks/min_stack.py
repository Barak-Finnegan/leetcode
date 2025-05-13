# https://leetcode.com/problems/min-stack/description/

class MinStack:

    def __init__(self):
        self.__min_map = {}
        self.__stack = []
        self.__min_index = None

    def push(self, val: int) -> None:
        if self.__min_index is None:
            self.__min_index = 0
            self.__min_map[0] = None
        elif self.__stack[self.__min_index] >= val:
            self.__min_map[len(self.__stack)] = self.__min_index
            self.__min_index = len(self.__stack)

        self.__stack.append(val)

    def pop(self) -> None:
        self.__stack.pop()

        if len(self.__stack) in self.__min_map:
            self.__min_index = self.__min_map[len(self.__stack)]
            del self.__min_map[len(self.__stack)]
            

    def top(self) -> int:
        return self.__stack[-1]

    def getMin(self) -> int:
        return self.__stack[self.__min_index]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
