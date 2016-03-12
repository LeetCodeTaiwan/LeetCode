class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
          return False

        max = float("inf")
        min = nums[0]
        for x in xrange(0,len(nums)-1):
            if nums[x] < nums[x+1]:
                if max > nums[x+1]:
                  max = nums[x+1]
                elif max < nums[x+1]:
                  return True
                if min < nums[x]:
                  return True
                else:
                  min = nums[x]
        return False

# Test Case
# s = Solution()
# print s.increasingTriplet([5,1,5,5,2,5,4]) # True
# print s.increasingTriplet([1,2,1,2,1,2,1,2,1,2]) # False
