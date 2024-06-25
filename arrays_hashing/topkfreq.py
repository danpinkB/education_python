from collections import defaultdict, Counter


class Solution(object):
    def topKFrequent(self, nums, k):
        kfreqmap = defaultdict(int)
        for i, num in enumerate(nums):
            kfreqmap[num] = kfreqmap.get(num, 0)+1
        return [k_ for k_, v_ in sorted(kfreqmap.items(), key=lambda item: item[1], reverse=True)[0:k]]


if __name__ == "__main__":
    print(Solution().topKFrequent([4,1,-1,2,-1,2,3],2))

