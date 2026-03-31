# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def merge(self, L: List[Pair], R: List[Pair]) -> List[Pair]:
        left_ptr, right_ptr = 0, 0
        new_arr = []
        while left_ptr < len(L) and right_ptr < len(R):
            if L[left_ptr].key <= R[right_ptr].key:
                new_arr.append(L[left_ptr])
                left_ptr += 1
            else:
                new_arr.append(R[right_ptr])
                right_ptr += 1
        
        if left_ptr < len(L):
            new_arr.extend(L[left_ptr:])
        else:
            new_arr.extend(R[right_ptr:])

        return new_arr

    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if pairs == []:
            return []

        if len(pairs) == 1:
            return pairs

        left_arr = self.mergeSort(pairs[:len(pairs)//2])
        right_arr = self.mergeSort(pairs[len(pairs)//2:])
        return self.merge(left_arr, right_arr)