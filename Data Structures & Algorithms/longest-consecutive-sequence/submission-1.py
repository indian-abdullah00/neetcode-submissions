class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        bigges = 0
        for num in numSet:
            if num -1 in numSet:
                continue
            length = 1
            while  num + length in numSet:
                length += 1
            
            bigges = max(length, bigges)

        return bigges
