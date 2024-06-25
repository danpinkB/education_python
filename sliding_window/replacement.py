from collections import defaultdict


class Solution(object):
    def characterReplacement(self, s, k):
        if len(s) <= 1: return len(s)
        symbols = defaultdict(int)
        sublen = 0
        max_ = 0
        for i in range(len(s)):
            symbols[s[i]] += 1
            max_ = max(max_, symbols[s[i]])
            print(symbols)
            print(max_)
            if max_ + k > sublen:
                sublen += 1
            else:
                symbols[s[i-sublen]] -= 1

        return sublen


if __name__ == "__main__":
    # print(Solution().characterReplacement("ABAB", 2))
    print(Solution().characterReplacement("AABABBA", 1))
    # print(Solution().characterReplacement("AAAA", 0))
