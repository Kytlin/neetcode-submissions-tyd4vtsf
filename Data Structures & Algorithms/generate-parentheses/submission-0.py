class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def findParenStr(paren_str, l, r):
            if r < l or (r >= 0 and l < 0):
                return

            if l == 0:
                res.append(paren_str + ")" * r)
                return

            findParenStr(paren_str + "(", l-1, r)
            findParenStr(paren_str + ")", l, r-1)

        findParenStr("", n, n)
        return res
            