class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = float("inf")
        

    def push(self, val: int) -> None:
        self.minimum = min(self.minimum, val)
        self.stack.append((val, self.minimum))
        

    def pop(self) -> None:
        self.stack.pop(-1)
        if not self.stack:
            self.minimum = float("inf")
        else:
            self.minimum = self.stack[-1][1]

        

    def top(self) -> int:
        return self.stack[-1][0]

    
    def getMin(self) -> int:
        return self.minimum
        
