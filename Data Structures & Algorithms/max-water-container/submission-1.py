from math import ceil
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        pointer_1 = 0
        pointer_2 = len(heights) - 1
        while pointer_1 < pointer_2:
            water = (min(heights[pointer_1],heights[pointer_2]))*(pointer_2-pointer_1)
            if water > max_water:
                max_water = water
            if heights[pointer_1] > heights[pointer_2]:
                pointer_2 -= 1
            else:
                pointer_1 += 1

        return max_water

            
    



             

            
        