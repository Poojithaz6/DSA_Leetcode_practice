class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums)
        sum2=0
        sum=(n*(n+1))//2
        for num in nums:
            sum2+=num
        return sum-sum2
