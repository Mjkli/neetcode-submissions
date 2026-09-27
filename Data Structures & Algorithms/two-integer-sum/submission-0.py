class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        right = len(nums) - 1
        for i, val in enumerate(nums):
            for j, val_2 in enumerate(nums):
                if j == i:
                    continue
                if val + val_2 == target:
                    return [i,j]


        return []