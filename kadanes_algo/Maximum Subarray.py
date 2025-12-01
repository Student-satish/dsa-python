class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0;
        maxSum = float('-inf');
        for i in range(0,len(nums)):
            currSum = max(currSum+nums[i],nums[i]);
            maxSum = max(currSum,maxSum);
        
        return maxSum;
        