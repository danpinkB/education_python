class Solution(object):
    def isPalindrome(self, s:str):
        normalized = [ch.lower() for ch in s if ch.isalnum()]
        slen = len(normalized)
        for i in range(slen):
            if normalized[i] != normalized[slen-i-1]: return False
        return True


if __name__ == "__main__":
    print(Solution().isPalindrome("0P"))
