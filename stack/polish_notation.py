class Solution(object):
    operations = {
        '*': lambda x,y:x*y,
        '/': lambda x,y:x/y,
        '+': lambda x,y:x+y,
        '-': lambda x,y:x-y,
    }

    def evalRPN(self, tokens):
        stack = []
        res = 0
        a = 0
        b = 0
        for token in tokens:
            if token in '*-+/':
                a = stack.pop()
                b = stack.pop()
                res = int(self.operations[token](b, a))
                stack.append(res)
            else:
                stack.append(int(token))
        return res


if __name__ == "__main__":
    print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))