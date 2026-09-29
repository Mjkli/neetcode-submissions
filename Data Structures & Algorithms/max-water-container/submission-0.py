class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ptr1 = 0
        ptr2 = len(heights) - 1
        max_out = 0
        while ptr1 < ptr2:
            width = ptr2 - ptr1
            height = min(heights[ptr1], heights[ptr2])
            poss_max = width * height

            if poss_max > max_out:
                max_out = poss_max
            
            if heights[ptr1] > heights[ptr2]:
                ptr2 -= 1
            elif heights[ptr1] < heights[ptr2]:
                ptr1 += 1
            else:
                ptr2 -= 1
                ptr1 += 1

        return max_out 
