class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack:
            if self.min_stack[-1][0] > val:
                self.min_stack.append([val,len(self.stack)-1])   
        else:
            self.min_stack.append([val,len(self.stack)-1])  
        return
        

    def pop(self) -> None:
        if len(self.stack) - 1 == self.min_stack[-1][1]:
            self.min_stack.pop()
        self.stack.pop()
        return
        

    def top(self) -> int:
        
        return self.stack[-1]
        

    def getMin(self) -> int:
        print(self.min_stack[-1][0])
        return self.min_stack[-1][0]
        
