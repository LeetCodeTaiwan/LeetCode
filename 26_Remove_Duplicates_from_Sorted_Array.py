class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
          return 0
        prev = nums[0]
        i = 1
        lastIndex = len(nums) - 1
        while i <= lastIndex:
            if nums[i] == prev :
                lastIndex -= 1
                nums.pop(i)
            else:
                prev = nums[i]
                i += 1
        return lastIndex + 1

class Solution2(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def handleZeroCase(num):
          return num if num != 0 else 1
        try:
          prev = nums[0]
          i = 1
          while handleZeroCase(nums[i]):
              if nums[i] == prev :
                  nums.pop(i)
              else:
                  prev = nums[i]
                  i += 1
        except Exception, e:
          return len(nums)

s = Solution()
s2 = Solution2()
print s.removeDuplicates([1,1,1,1,1,1,1])
print s.removeDuplicates([0,0,0,0,0,0])