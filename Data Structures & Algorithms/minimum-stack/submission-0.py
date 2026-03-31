class MinStack:

    def __init__(self):
        self.elem_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if self.min_stack == [] or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        self.elem_stack.append(val)

    def pop(self) -> None:
        if self.elem_stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.elem_stack.pop()

    def top(self) -> int:
        return self.elem_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
