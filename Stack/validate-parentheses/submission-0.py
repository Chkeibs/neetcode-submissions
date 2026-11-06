class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for c in s:
            if c not in pairs:
                stack.append(c)

            else:
                if not stack or stack.pop() != pairs[c]:
                    return False

        return not stack