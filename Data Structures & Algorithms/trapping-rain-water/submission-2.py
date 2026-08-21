class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        leftmax = height[l]
        rightmax = height[r]
        l+=1
        r-=1
        water = 0
        while l<=r:
            if leftmax <= rightmax:
                water += max(min(leftmax,rightmax) - height[l],0)
                leftmax = max(leftmax,height[l])
                l += 1
        
            else:
                water += max(min(leftmax,rightmax) - height[r],0)
                rightmax = max(rightmax,height[r])
                r -= 1
        return water


        

            

        