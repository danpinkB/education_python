class Solution(object):
    def trap(self, height):
        if len(height) < 3:
            return 0
        i = 0
        j = len(height) - 1
        water = 0
        while i < j:
            level = min(height[i], height[j])
            while i < j and height[i] <= level:
                water += level-height[i]
                i += 1
            while i < j and height[j] <= level:
                water += level-height[j]
                j -= 1
        return water


if __name__ == "__main__":
    print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(Solution().trap([4,2,0,3,2,5]))