import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            x = stones[0]
            y = stones[1]
            if x == y:
                heapq.heappop_max(stones)
                heapq.heappop_max(stones)
            elif x > y:
                x = heapq.heappop_max(stones)
                y = heapq.heappop_max(stones)
                heapq.heappush_max(stones, x - y)

        if stones:
            return heapq.heappop(stones)
        else:
            return 0
            