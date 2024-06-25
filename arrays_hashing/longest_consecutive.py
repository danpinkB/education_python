from collections import defaultdict


class Solution(object):
    def longestConsecutive(self, nums):
        existed_numbers = set(nums)
        max_ = 0
        counter = 0
        for num in nums:
            if num-1 in existed_numbers: continue
            counter = 0
            while num + counter in existed_numbers:
                counter += 1
            max_ = max(max_, counter)
        return max_


if __name__ == "__main__":
    print(Solution().longestConsecutive([100,4,200,1,3,2]))
