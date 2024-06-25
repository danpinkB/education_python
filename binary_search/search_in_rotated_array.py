import time
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        k: int
        while l <= r:
            k = (l + r) // 2
            if nums[k] == target:
                return k

            if nums[l] <= nums[k]:
                if target > nums[k] or nums[l] > target:
                    l = k+1
                else:
                    r = k-1
            else:
                if target < nums[k] or target > nums[r]:
                    r = k-1
                else:
                    l = k+1
        return -1


if __name__ == "__main__":
    print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))
    print(Solution().search([4, 5, 6, 7, 0, 1, 2], 3))
    print(Solution().search([1], 0))
    print(Solution().search([1], 1))
    print(Solution().search([4,5,6,7,0,1,2], 5))
    print(Solution().search([1,2,3,4,5,6], 4))
    print(Solution().search([8,1,2,3,4,5,6,7], 6))
    print(Solution().search([5,1,2,3,4], 1))
