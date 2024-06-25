from typing import List


class Solution(object):
    def containsDuplicate(self, nums: List[int]) -> bool:
        existed_numbers = {}
        for num in nums:
            if existed_numbers.get(num):
                return True
            existed_numbers[num] = True

        return False
