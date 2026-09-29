class Solution:
    def isValid(self, s: str) -> bool:
        left_map = {'(': ')', '{': '}', '[' : ']'}
        stack = []
        for i, val in enumerate(s):
            if val in left_map.keys():
                stack.append(val)
                continue
            if len(stack) > 0:
                last_val = stack.pop()
            else:
                return False
            if left_map[last_val] != val:
                return False


        if len(stack) == 0:
            return True
        
        return False
