class Solution(object):
    def threeSum(self, nums):
        nlen = len(nums)
        if nlen < 3: return []
        nums.sort()
        triples = set()
        j = 0
        k = 0
        sum_ = 0
        for i in range(nlen):
            j = i+1
            k = nlen-1
            while j < k:
                sum_ = nums[i]+nums[j]+nums[k]
                if sum_ == 0:
                    triples.add((nums[i], nums[j], nums[k]))
                if sum_ < 0:
                    j += 1
                else:
                    k -= 1
        return [list(triple) for triple in triples]


if __name__ == "__main__":
    print(Solution().threeSum([-1,0,1,2,-1,-4]))
