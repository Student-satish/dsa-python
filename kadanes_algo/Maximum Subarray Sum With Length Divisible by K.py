class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums);
        prefixSum = [0];
        for i in range(n):
            prefixSum.append(prefixSum[-1]+nums[i]);
        
        maxSubSum = float('-inf');
        for i in range(n-k+1):
            for j in range(i+k,n+1,k):
                maxSubSum = max(maxSubSum,prefixSum[j]-prefixSum[i]);
        

        return maxSubSum;

        
class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums);
        prefixSum = [0];
        for i in range(n):
            prefixSum.append(nums[i] + prefixSum[-1]);
        
        maxSubSum = prefixSum[k];
        for i in range(0,k):
            currSum = 0;
            for j in range(i,n-k+1,k):
                l = j + k - 1;
                currSum = max(currSum+prefixSum[l+1]-prefixSum[j],prefixSum[l+1]-prefixSum[j]);
                maxSubSum = max(currSum,maxSubSum);

        return maxSubSum;