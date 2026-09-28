class Solution:
    def isValid(self, s: str) -> bool:
        left_map ={'[': ']', '(': ')', '{':'}'}
        list_s = list(s)
        stack = []
        for i, val in enumerate(list_s):
            if val in left_map.keys():
                stack.append(val)
            if val in left_map.values():
                if len(stack) == 0:
                    return False
                if len(stack) != 0 and left_map[stack.pop()] != val:
                    return False
                print(val)


        if len(stack) > 0:
            return False
        return True