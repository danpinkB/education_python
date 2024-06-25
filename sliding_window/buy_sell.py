class Solution(object):
    def maxProfit(self, prices):
        max_ = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i]-buy > max_:
                max_ = prices[i]-buy
        return max_


if __name__ == "__main__":
    # print(Solution().maxProfit([7,1,5,3,6,4]))
    # print(Solution().maxProfit([2,1,4]))
    print(Solution().maxProfit([[2,4,1]]))