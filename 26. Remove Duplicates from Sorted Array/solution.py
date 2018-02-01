class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        my_num = reduce(lambda x, y: x if x[-1] == y[0] else x + y, [[i] for i in nums] if nums else [[]])
        del nums[:]
        nums += my_num
        return len(nums)
        