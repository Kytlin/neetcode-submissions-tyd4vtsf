class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        
        mem = []
        for t in tokens:
            if t.isnumeric() or t[0] == "-" and t[1:].isnumeric():
                mem.append(t)
            else: # token is an operation
                # mem is non-empty since valid input

                num1 = int(mem.pop())
                num2 = int(mem.pop())
                if t == "+":
                    mem.append(num1 + num2)
                if t == "-":
                    mem.append(num2 - num1)
                if t == "*":
                    mem.append(num1 * num2)
                if t == "/":
                    mem.append(num2 // num1)
                    if mem[-1] < 0 and num2 % num1 != 0:
                        mem[-1] += 1

        return mem[0]  # tokens should only contain one element