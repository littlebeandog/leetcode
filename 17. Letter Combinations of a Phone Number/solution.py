class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = {1: "", 2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz", 0: " "}
        r = [''] if digits else []
        for num in digits:
            l = []
            for ch in d[int(num)]:
                l += [s + ch for s in r]
            r = l
        return r