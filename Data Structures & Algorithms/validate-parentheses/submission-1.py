class Solution:
    def isValid(self, s: str) -> bool:
        cur_open_brackets = []
        bracket_map = {")": "(", "]": "[", "}": "{"}
        for bracket in s:
            if bracket == "(" or bracket == "[" or bracket == "{":
                cur_open_brackets.append(bracket)
            elif cur_open_brackets != [] and cur_open_brackets[-1] == bracket_map[bracket]:
                cur_open_brackets.pop()
            else:
                return False

        if cur_open_brackets != []:
            return False
        return True