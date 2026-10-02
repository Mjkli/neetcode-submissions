class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        found = set()
        for i, n in enumerate(nums):
            found.add(n)
            if len(found) - 1 < i:
                return n