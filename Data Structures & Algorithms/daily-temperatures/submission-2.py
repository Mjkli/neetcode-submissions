class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0] * len(temperatures)
        stack = []
        for i, val in enumerate(temperatures):
            while len(stack) > 0 and temperatures[stack[-1]] < val:
                j = stack.pop()
                out[j] = i - j


            stack.append(i)
        return out