class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []

        for ch in s:
            if ch == '(':
                stack.append(ch)
            else:  # when ch == ')'
                if stack[-1] == '(':
                    # "()" => score 1
                    stack.pop()
                    stack.append(1)
                else:
                    # "(A)" => 2 * score(A)
                    inner_score = 0
                    while stack[-1] != '(':
                        inner_score += stack.pop()
                    stack.pop()  # remove '('
                    stack.append(2 * inner_score)

        # Sum up all scores in stack (for "AB" case)
        return sum(stack)
