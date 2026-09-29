class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort_nums = sorted(nums)
        out = []
        for i, val in enumerate(sort_nums):
            ptr1 = i +1
            ptr2 = len(nums) - 1
            while ptr1 < ptr2:
                poss_sum = val + sort_nums[ptr1] + sort_nums[ptr2]
                if poss_sum == 0 and ptr1 != i and ptr2 != i:
                    poss_val = [val,sort_nums[ptr1],sort_nums[ptr2]]
                    if poss_val not in out:
                        out.append(poss_val)
                    ptr1 += 1
                    ptr2 -= 1
                if poss_sum > 0:
                    ptr2 -= 1
                if poss_sum < 0:
                    ptr1 += 1
        
        return out