class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res = ''
        for i in s:
            temp = ord(i) - 96
            res += str(temp)

        for i in range(k):
            res = sum(int(x) for x in res)
            res = str(res)
        return int(res)