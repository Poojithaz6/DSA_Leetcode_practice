class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        ans=[]
        n=len(nums)
        for i in range(n):
            ans.append(nums[nums[i]])
        return ans
