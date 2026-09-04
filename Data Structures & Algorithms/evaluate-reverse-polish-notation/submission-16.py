class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        if len(tokens) == 1:
            return(int(tokens[0]))

        def evaluate(val, NUM1, NUM2):
            num1,num2 = int(NUM1),int(NUM2)
            if val == '+':
                return num1+num2
            if val == '-':
                return num1-num2
            if val == '*':
                return num1*num2
            if val == '/':
                return int(num1/num2)

        num = []
 
        for item in tokens:
            if item not in ['+', '-', '*', '/']:
                num.append(item)
            else:
                num1 = num.pop() # 3
                num2 = num.pop() # 4
                num.append(evaluate(item,num2,num1))
        return num[0]