class Solution(object):
    def largestRectangleArea(self, heights):

        # print([k for k in stack])
        stack = []
        max_ = 0
        for height in heights:
            c = 1
            while stack and stack[-1] > height:
                h = stack.pop()
                max_ = max(max_, h * c)
                c += 1
            for i in range(c):
                stack.append(height)
        c = 1
        while stack:
            max_ = max(max_, stack.pop()*c)
            c += 1
        return max_


        # return max(max_, stack[-1]*len(stack)) if stack else max_


if __name__ == "__main__":
    # print(Solution().largestRectangleArea([4,2,0,3,2,5]))
    # print(Solution().largestRectangleArea([0,9]))
    print(Solution().largestRectangleArea([5,4,1,2]))