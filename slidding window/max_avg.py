class Solution:
    def findMaxAverage(self, nums, k):
        self.total_sum=sum(nums[:k])
        self.max_avg=self.total_sum/k

        for i in range(len(nums)-k):
            self.total_sum =(self.total_sum-nums[i])+nums[i+k]

            self.max_avg=max(self.max_avg,self.total_sum/k)

        return self.max_avg


# nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
        
# nums = [1,12,-5,-6,50,3]
# k = 4
nums=[5]
k=1

s1=Solution()

a=s1.findMaxAverage(nums,k)

print(a)