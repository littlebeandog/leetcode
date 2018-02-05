# Time limit exceeded
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = []
        for one_str in strs:
            i = 0
            while i < len(res):
                if self.is_anagram(one_str, res[i][0]):
                    break
                i += 1
            if i == len(res):
                res.append([one_str])
            else:
                res[i].append(one_str)
        return res
    
    def is_anagram(self, str1, str2):
        if len(str1) != len(str2):
            return False
        str2_list = list(str2)
        for ch in str1:
            if ch not in str2_list:
                return False
            else:
                str2_list.remove(ch)
        return True if not str2_list else False

# O(k*N)
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = collections.defaultdict(list)
        for one_str in strs:
            ords = [0] * 26
            for ch in one_str:
                ords[ord(ch) - ord('a')] += 1
            res[tuple(ords)].append(one_str)
        return res.values()