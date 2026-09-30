class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0] * len(temperatures)
        stack = []
        for i, val in enumerate(temperatures):
            if len(stack) > 0 and stack[-1][1] < val:
                while len(stack) > 0 and stack[-1][1] < val:
                    j, s_val = stack.pop()
                    out[j] = i - j


            stack.append((i,val))
        return out