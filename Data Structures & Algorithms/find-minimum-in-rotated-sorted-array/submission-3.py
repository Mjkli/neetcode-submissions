class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        sort_nums = sorted(nums)
        print(nums, sort_nums)
        return sort_nums[0]
       # while left <= right:
       #     mid = int((left + right) / 2)
       #     if left == mid and right == mid:
       #         return sort_nums[mid]
       #     if sort_nums[left] <= sort_nums[mid]:
       #         right = mid - 1
            #else:
                #left = mid + 1


            