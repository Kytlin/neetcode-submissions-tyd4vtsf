import copy

# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        intermediate_res = [pairs]
        cur_pairs = copy.deepcopy(pairs)

        if pairs == []:
            return []
            
        for i in range(1,len(pairs)):
            swap_idx = i
            cur_pairs = copy.deepcopy(cur_pairs)
            while swap_idx > 0 and cur_pairs[swap_idx].key < cur_pairs[swap_idx-1].key:
                cur_pairs[swap_idx], cur_pairs[swap_idx-1] = cur_pairs[swap_idx-1], cur_pairs[swap_idx]
                swap_idx -= 1
            intermediate_res.append(cur_pairs)
        return intermediate_res