class Solution(object):
    def maxArea(self, height):
        if len(height) == 2: return min(height[0], height[1])
        i = 0
        j = len(height)-1
        max_area = 0
        while i < j:
            max_area = max(max_area, min(height[i], height[j])*(j-i))
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
        return max_area

if __name__ == "__main__":
    print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
