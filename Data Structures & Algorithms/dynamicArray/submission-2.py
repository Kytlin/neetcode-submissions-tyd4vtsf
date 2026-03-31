class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [0] * capacity
        self.size = 0
        self.cap = capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.cap:
            self.resize()
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        last_num = self.arr[self.size-1]
        self.size -= 1
        return last_num

    def resize(self) -> None:
        self.cap *= 2
        new_arr = [0] * self.cap

        for i in range(len(self.arr)):
            new_arr[i] = self.arr[i]

        self.arr = new_arr

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.cap