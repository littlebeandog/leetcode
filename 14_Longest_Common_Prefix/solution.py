class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        rs = ""
        i = 0
        while strs:
            j = 0
            for j in range(len(strs)):
                if i >= len(strs[j]):
                    break
                elif strs[j][i] == strs[0][i]:
                    j += 1
                else:
                    break
            if j == len(strs):
                rs += strs[0][i]
                i += 1
            else:
                break
        return rs
        
# reduce version
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        return reduce(self.common_prefix, strs) if strs else ''
    
    def common_prefix(self, str1, str2):
        if not str1 or not str2:
            return ''
        else:
            i = 0
            while i < min(len(str1), len(str2)):
                if str1[i] != str2[i]:
                    break
                i += 1
            return str1[:i]
        