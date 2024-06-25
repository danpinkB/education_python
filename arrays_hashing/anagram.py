class Solution(object):
    def isAnagram(self, s, t):
        s_chars = {}
        for sch in s:
            s_chars[sch] = s_chars.get(sch, 0) + 1
        chind = 0
        for tch in t:
            chind = s_chars.get(tch, 0)
            if chind == 0: return False
            if chind - 1 == 0:
                s_chars.pop(tch)
            else: s_chars[tch] = s_chars.get(tch, 0) - 1
        return len(s_chars) == 0


if __name__ == "__main__":
    Solution().isAnagram("anagram", "nagaram")