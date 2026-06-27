from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = defaultdict(int)
        freq = [[] for i in range(len(nums)+1) ]
        output = []

        for num in nums:
            num_count[num] += 1
        
        for num, count in num_count.items():
            freq[count].append(num)
        
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                output.append(num)
                if len(output) == k:
                    return output


        
        

        
        return output


                