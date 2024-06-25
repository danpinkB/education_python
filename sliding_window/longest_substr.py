class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) <= 1: return len(s)
        max_ = 0
        sub = []
        for i in range(len(s)):
            if s[i] in sub:
                max_ = max(max_, len(sub))
                while sub.pop(0) != s[i]: pass
            sub.append(s[i])
        return max(max_, len(sub))


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("aew"))