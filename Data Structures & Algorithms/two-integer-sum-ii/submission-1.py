class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) - 1

        while left< right:
            sum_number = numbers[left] + numbers[right]

            if sum_number < target:
                left += 1
            
            elif sum_number > target:
                right -=1

            else:
                return [left + 1, right +1]

        