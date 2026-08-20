class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triple = []
        for i , a in enumerate(nums):
            if a > 0 or i >= len(nums)-2:
                break
            if i > 0 and a == nums[i-1]:
                continue
            j = i +1
            k = len(nums)-1
            while j<k:
                threesum = a + nums[j] + nums[k]

                if threesum < 0:
                    j = j+1
                elif threesum > 0:
                    k = k-1
                else:
                    triple.append([a,nums[j],nums[k]])
                    while j<k and nums[j] == nums[j + 1]:
                        j += 1
                    while j<k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
        return triple
            
