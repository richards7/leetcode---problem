class Solution(object):
    def longestCommonPrefix(self, strs):
        res = strs[0]
        for s in strs:
            while not s.startswith (res):
                res = res[:-1]
        return res