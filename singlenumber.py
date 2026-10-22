class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        for x in nums:
            if nums.count(x) == 1:
                return x
