from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = defaultdict(int)
        output = []

        for num in nums:
            num_count[num] += 1
        
        print((sorted(num_count.items(), key = lambda item: item[1])))
        for i,pair in enumerate(sorted(num_count.items(), key = lambda item: item[1],reverse=True)):
            key,value = pair
            if i == k:
                break
            output.append(int(key))
        
        return output


                