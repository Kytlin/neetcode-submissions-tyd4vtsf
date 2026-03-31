# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSortHelper(self, pairs, left, right):
        if right - left + 1 <= 1:
            return pairs

        pivot = pairs[right]
        head, tail = left, left
        while tail < right:
            if pairs[tail].key < pivot.key:
               pairs[tail], pairs[head] = pairs[head], pairs[tail]
               head += 1
            tail += 1
        
        pairs[right] = pairs[head]
        pairs[head] = pivot

        self.quickSortHelper(pairs, left, head-1) 
        self.quickSortHelper(pairs, head+1, right)

        return pairs

    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.quickSortHelper(pairs, 0, len(pairs)-1)

