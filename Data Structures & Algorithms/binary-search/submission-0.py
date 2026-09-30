class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left_index = 0
        right_index = len(nums) - 1
        while left_index <= right_index:
            half = int((left_index + right_index) / 2)
            if nums[half] == target:
                return half
            elif nums[half] < target:
                left_index = half + 1
            else:
                right_index = half - 1
        
        return -1

            
            
