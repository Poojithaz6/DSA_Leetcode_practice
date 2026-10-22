class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        arr = list(t)

        for x in s:
            arr.remove(x)

        return arr[0]
