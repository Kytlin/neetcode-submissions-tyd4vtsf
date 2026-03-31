class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(paren_str, left_count, right_count):
            if left_count == 0 and right_count == 0:
                res.append(paren_str)
                return

            if left_count > 0:
                backtrack(paren_str + "(", left_count - 1, right_count)
            if right_count > 0 and left_count < right_count:
                backtrack(paren_str + ")", left_count, right_count - 1)

        backtrack("", n, n)
        return res