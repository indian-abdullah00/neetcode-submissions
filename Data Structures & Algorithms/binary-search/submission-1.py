class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) -1
        while True:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid
            else:
                l = mid
            if l + 1 == r:
                if nums[r] ==target:
                    return r
                elif nums[l] == target:
                    return l
                else:
                    return -1
            if l == r :
                return -1 

        