class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        ans = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and nums[i] not in ans:
                    ans.append(nums[i])

        return ans
