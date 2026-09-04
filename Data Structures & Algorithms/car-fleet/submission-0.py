class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [(target-p)/s for p,s in zip(position,speed)]
        cars = list(zip(position,time))
        
        cars.sort()
        # print(cars)

        stack = []

        for item in cars:
            while stack and stack[-1][1] <= item[1]:
                # print(stack[-1][1],item[1])
                stack.pop()
            stack.append(item)

        return(len(stack))