class Solution(object):
    def twoSum(self, nums, target):
        nums_indexes = {}
        nind = 0
        for i, num in enumerate(nums):
            nind = nums_indexes.get(target - num)
            if nind is not None: return [nind, i]
            nums_indexes[num] = i

if __name__ == "__main__":
    print(Solution().twoSum([2,7,11,15], 9))
