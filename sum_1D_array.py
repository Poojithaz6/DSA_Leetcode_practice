class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        ans = []
        sm = 0

        for x in nums:
            sm += x
            ans.append(sm)

        return ans
