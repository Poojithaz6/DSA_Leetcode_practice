class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        ans = []

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        arr = sorted([nums[i], nums[j], nums[k]])
                        if arr not in ans:
                            ans.append(arr)

        return ans
