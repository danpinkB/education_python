class Solution(object):
    brackets = {
        '}':'{',
        ')':'(',
        ']':'[',
    }

    def isValid(self, s):
        if len(s) %2 !=0: return False
        stack = []
        for ch in s:
            if ch in "{([":
                stack.append(ch)
            elif len(stack)==0 or stack.pop() != self.brackets[ch]:
                return False
        return not stack


if __name__ == "__main__":
    print(Solution().isValid('()[]{}'))