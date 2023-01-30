class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mid = len(nums)//2
        lptr, rptr = mid-1, mid+1

        if len(nums) < 2:
            return len(nums)

        if (nums[lptr] == 0 or nums[rptr] == 0):
            while (lptr > 0 and rptr < len(nums)):
                if nums[lptr] != 0:
                    if nums[mid] > 0:
                        return len(nums[:mid+1])
                    else:
                        return len(nums[:lptr+1])
                if nums[rptr] != 0:
                    if nums[mid] < 0:
                        return len(nums[mid:])
                    else:
                        return len(nums[rptr:])
                lptr -= 1
                rptr += 1
            return 0
        else:
            maxi = 0
            if (nums[mid] < 0):
                for i in range(mid, len(nums)):
                    if nums[i] < 0:
                        maxi += 1
                return maxi + len(nums[:mid])
            else:
                for i in range(0, mid):
                    if nums[i] > 0:
                        maxi += 1
                print(maxi)
                return maxi + len(nums[mid:])


s = Solution()

nums = [-2, -1, -1, 1, 2, 3]
print(s.maximumCount(nums))
