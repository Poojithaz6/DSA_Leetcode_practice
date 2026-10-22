class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        arr=[]
        for i in range(len(numbers)):
            find=target-numbers[i]
            if find in numbers:
                j=numbers.index(find)
                if i<j:
                    arr.append(i+1)
                    arr.append(j+1)
                    return arr
                if i>j:
                    arr.append(j+1)
                    arr.append(i+1)
                    return arr
                if i==j:
                    continue
        
