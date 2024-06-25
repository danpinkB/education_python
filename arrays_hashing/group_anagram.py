from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        return anagram_map.values()


if __name__ == "__main__":
    print(Solution().groupAnagrams(["tin","ram","zip","cry","pus","jon","zip","pyx"]))
