class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = []
        self.size = 0
        self.cap = capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        self.arr.append(n)
        if self.size == self.cap:
            self.cap *= 2
        self.size += 1

    def popback(self) -> int:
        last_num = self.arr.pop()
        self.size -= 1
        return last_num

    def resize(self) -> None:
        if self.size == self.cap:
            self.cap *= 2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.cap