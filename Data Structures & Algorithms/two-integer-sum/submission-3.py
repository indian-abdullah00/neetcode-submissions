from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_num = defaultdict(int)

        for i,num in enumerate(nums):
            dict_num[num] = i
        
        for i,num in enumerate(nums):
            search = target - num
            if search in dict_num:
                if i == dict_num[search]:
                    continue
                return list([i,dict_num[search]])
        