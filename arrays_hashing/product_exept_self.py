class Solution(object):
    def productExceptSelf(self, nums):
        zcount = 0
        zindex = 0
        mul = 1
        for i, num in enumerate(nums):
            if num == 0:
                zcount += 1
                zindex = i
            else:
                mul *= num
        if zcount > 1: return [0] * len(nums)
        res = [0] * len(nums)
        if zcount == 1:
            res[zindex] = mul
            return res
        return [mul/num for num in nums]
