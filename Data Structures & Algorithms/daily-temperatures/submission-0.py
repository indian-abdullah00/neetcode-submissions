class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)
        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append([temp,i])
                continue
            while stack and stack[-1][0] < temp:
                item = stack.pop()
                result[item[1]] = i - item[1] 
            stack.append([temp,i])

        return result
            

        