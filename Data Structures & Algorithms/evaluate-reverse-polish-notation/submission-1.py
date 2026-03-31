class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        ops = {'+','-','*','/'}

        if len(tokens) == 1:
            return int(tokens[0])

        for t in tokens:
            if t in ops:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                if t == "+":
                    res = num1 + num2
                if t == "-":
                    res = num2 - num1
                if t == "*":
                    res = num1 * num2
                if t == "/":
                    res = int(num2 / num1)
                stack.append(res)
            else:
                stack.append(t)
        return stack[-1]