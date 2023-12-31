class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for item in s:
            if item in dict.values():
                stack.append(item)
            elif item in dict.keys():
                if stack == [] or dict[item] != stack.pop():
                    return False
            else:
                return False
        return stack == []
        