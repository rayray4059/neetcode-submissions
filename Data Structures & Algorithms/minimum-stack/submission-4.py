class MinStack:

    def __init__(self):
        self.stack = []
        self.min_elem = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_elem or val <= self.getMin(): 
            self.min_elem.append(val)

    def pop(self) -> None:
        curr = self.stack.pop()
        if self.getMin() == curr:
            self.min_elem.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return "null"

    def getMin(self) -> int:
        return self.min_elem[-1]
