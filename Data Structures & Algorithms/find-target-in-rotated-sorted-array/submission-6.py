class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0 
        r = len(nums) -1
        res = -1

        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                res = m
                break
            elif nums[l] <= nums[m]:
                if nums[l] <= target <= nums[m]:
                    r = m-1
                    continue
                l = m+1
            else: 
                if nums[m] <= target and target <= nums[r]:
                    l = m+1
                    continue
                r = m-1
        return res

        