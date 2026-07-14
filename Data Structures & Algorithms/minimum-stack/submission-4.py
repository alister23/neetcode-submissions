class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = float("inf")

    def push(self, val: int) -> None:
        self.min_val = min(self.min_val, val)
        self.stack.append((val, self.min_val))

    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self.min_val = self.getMin()
        else:
            self.min_val = float('inf')

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
