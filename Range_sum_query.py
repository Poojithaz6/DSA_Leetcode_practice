class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        sm = 0

        for i in range(left, right + 1):
            sm += self.nums[i]

        return sm
