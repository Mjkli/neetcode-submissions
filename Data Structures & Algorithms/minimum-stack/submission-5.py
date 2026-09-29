class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_val == None or self.min_val > val:
            self.min_val = val

    def pop(self) -> None:
        self.stack.pop()
        if len(self.stack) == 0:
            self.min_val = None
            return

        sort_stack = sorted(self.stack)
        if sort_stack[0] != self.min_val:
            self.min_val = sort_stack[0]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val
        
