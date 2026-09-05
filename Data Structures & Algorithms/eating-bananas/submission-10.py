from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_sum = sum(piles)
        max_banana = max(piles)
        min_banana= ceil(max_sum/h)

        def time_eat(pile, slot):
            count = 0
            for item in piles:
                count += ceil(item/slot)
            return count

        l = min_banana
        r = max_banana+1
        while l <= r:
            mid = (l+r)//2
            
            if time_eat(piles,mid) > h:
                l = mid+1
            elif time_eat(piles,mid) < h:
                r = mid-1
                current_best = mid
            elif time_eat(piles,mid) == h:
                r = mid-1
                current_best = mid

        return current_best

                




        