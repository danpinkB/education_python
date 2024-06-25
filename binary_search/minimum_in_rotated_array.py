import time
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r, res = 0, len(nums) - 1, nums[0]
        k: int
        while l<=r:
            if nums[l]<nums[r]:
                res = min(res, nums[l])
                break
            k = (r+l)//2
            res = min(res, nums[k])
            if nums[k] >= nums[l]:
                res = min(res, nums[l])
                l = k+1
            else:
                r = k-1

        return res


if __name__ == "__main__":
    print(Solution().findMin([3, 4, 5, 1, 2]))
    print(Solution().findMin([4, 5, 6, 7, 0, 1, 2]))
    print(Solution().findMin([2, 3, 1]))
    print(Solution().findMin([3, 1, 2]))
