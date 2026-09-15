class Solution(object):
    def checkSubarraySum(self, nums, k):
        remainder = {0: -1}
        prefix = 0

        for i, num in enumerate(nums):
            prefix = (prefix + num) % k

            if prefix in remainder:
                if i - remainder[prefix] >= 2:
                    return True
            else:
                remainder[prefix] = i

        return False
        