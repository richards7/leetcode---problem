class Solution(object):
    def findErrorNums(self, nums):
        for num in nums:
            i = abs(num) - 1

            if nums[i] < 0:
                duplicate = abs(num)
            else:
                nums[i] = -nums[i]

        for i in range(len(nums)):
            if nums[i] > 0:
                missing = i + 1
                break

        return [duplicate, missing]
        