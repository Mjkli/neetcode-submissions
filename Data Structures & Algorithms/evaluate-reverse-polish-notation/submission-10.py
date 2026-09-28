class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        out = None
        stack = []
        for i in tokens:
            if i == "+":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 + num2)
                continue
            if i == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 - num1)
                continue
            if i == "*":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1 * num2)
                continue
            if i == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num2 / num1))
                continue

            stack.append(int(i))

        return stack.pop()