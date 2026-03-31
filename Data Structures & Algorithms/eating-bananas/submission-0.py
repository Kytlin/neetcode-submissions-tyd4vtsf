class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:        
        piles.sort(reverse=True)

        lower, upper = 1, max(piles)
        best_so_far = upper
        while lower <= upper:
            rate = lower + (upper-lower) // 2
            time = 0
            for num_bananas in piles:
                time += math.ceil(num_bananas / rate)
                if time > h:
                    break
            if time <= h:
                best_so_far = min(best_so_far, rate)
                upper = rate - 1
            else:
                lower = rate + 1
        return best_so_far