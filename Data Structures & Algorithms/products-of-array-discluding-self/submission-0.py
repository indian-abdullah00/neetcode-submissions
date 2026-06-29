class Solution:

    def bruteForce(self, nums, index):
        answer = 1
        for i in range(0,len(nums)):
            if i == index:
                continue    
            answer *= nums[i]
        return answer

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = 1
        output = []
        for i in range(1,len(nums)):
            answer *= nums[i]
        
        output.append(int(answer))
        
        for i in range(1,len(nums)):
            if nums[i]==0:
                answer_key = self.bruteForce(nums, i)
                output.append(int(answer_key))
                continue
            factor = nums[i-1]/nums[i]
            answer*= factor
            output.append(int(answer))
        
        return output

            
        