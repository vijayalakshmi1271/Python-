class Solution:
    def isBalanced(self, s):
            # code here
        stack = []
        matching = {')': '(', '}': '{', ']': '['}
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:  # closing bracket
                if not stack or stack[-1] != matching[ch]:
                    return False
                stack.pop()
        return len(stack) == 0
    
            
            