class Solution(object):
    def twoSum(self, nums, target):
        arr=[]
        for i in range(len(nums)):
            find=target- nums[i]
            if find in nums:
                j=nums.index(find)
                if(i!=j):
                    arr.append(i)
                    arr.append(j)
                    return arr
        
