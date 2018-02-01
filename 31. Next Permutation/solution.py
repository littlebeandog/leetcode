class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            pass
        else:
            i = len(nums) - 1
            while i > 0:
                if nums[i] > nums[i - 1]:
                    break
                i -= 1
            nums[i:] = nums[:i - 1 if i else None: -1]
            if i:
                anchor = i - 1
                while i < len(nums):
                    if nums[i] > nums[anchor]:
                        tmp = nums[anchor]
                        nums[anchor] = nums[i]
                        nums[i] = tmp
                        break
                    i += 1