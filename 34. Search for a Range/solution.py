class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = int((start + end) / 2)
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                s_start,s_end = start, mid
                e_start,e_end = mid, end
                while s_start <= s_end:
                    s_mid = int((s_start + s_end) / 2)
                    if nums[s_mid] < target:
                        s_start = s_mid + 1
                    else:
                        s_end = s_mid - 1
                while e_start <= e_end:
                    e_mid = int((e_start + e_end) / 2)
                    if nums[e_mid] > target:
                        e_end = e_mid - 1
                    else:
                        e_start = e_mid + 1
                return [s_end + 1, e_start - 1]
        return [-1, -1]