import math
import time


class Solution(object):
    def minEatingSpeed(self, piles, h):
        l, r = 1, max(piles)
        res = r
        k = 0
        while l <= r:
            k = (l+r)//2
            hours = sum([math.ceil(p/k) for p in piles])
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1

        return res


if __name__ == "__main__":
    print(Solution().minEatingSpeed([3,6,7,11], 8))
    #print(Solution().minEatingSpeed([30,11,23,4,20], 6))