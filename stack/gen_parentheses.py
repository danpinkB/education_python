class Solution(object):
    def generateParenthesis(self, n):
        stack = []

        def gen(s, left, right):
            if left == n and right == n:
                return stack.append(s)
            if left < n:
                gen(s + "(", left + 1, right)
            if left > right:
                gen(s + ")", left, right + 1)

        gen('(', 1, 0)
        return stack




if __name__ == "__main__":
    print(Solution().generateParenthesis(3))