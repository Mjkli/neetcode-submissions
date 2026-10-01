class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = 1
        while left <= right:
            mid = int((left + right ) / 2)
            hours = 0
            for val in piles:
                hours += math.ceil(val / mid)
            
            if hours <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res
                