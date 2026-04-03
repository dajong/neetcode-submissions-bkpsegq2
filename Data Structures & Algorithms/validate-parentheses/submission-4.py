class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        mp = { "(":")", "[":"]", "{":"}"}
        closing = [")", "]", "}"]

        for i in range(len(s)):
            if s[i] in closing:
                if not stack or s[i] != mp[stack.pop()]:
                    return False
                else:
                    continue
            stack.append(s[i])
        return not stack