class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for val in tokens:
            if val == "+":
                out = stack.pop() + stack.pop()
            elif val == "-":
                top = stack.pop()
                bottom = stack.pop()
                out = bottom - top
            elif val == "*":
                out = int(stack.pop()) * int(stack.pop())
            elif val == "/":
                top = stack.pop()
                bottom = stack.pop()
                out = int(bottom / top)
            else:
                out = int(val)

            stack.append(out)
            
        if len(stack) > 1:
            return 0

        return stack[0]            
