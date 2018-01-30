class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            j, k = i + 1, len(nums) - 1
            while k > j:
                s = nums[i] + nums[j] + nums[k]
                if abs(s - target) < abs(res -target):
                    res = s
                # while k > j and nums[j] == nums[j + 1]:
                #     j += 1
                # while k > j and nums[k - 1] == nums[k]:
                #     k -= 1
                if s > target:
                    k -= 1
                elif s < target:
                    j += 1
                else:
                    break
        return res
