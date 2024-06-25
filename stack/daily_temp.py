from typing import List


class Solution(object):
    def dailyTemperatures(self, temperatures: List[int]):
        stack = []
        res = [0]*len(temperatures)
        for i in range(len(temperatures) - 1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            res[i] = 0 if not stack else stack[-1]-i
            stack.append(i)
        return res


if __name__ == "__main__":
    print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))