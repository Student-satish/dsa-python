# we have to remove the smallest subarray such that remaning sum of the array should be divisible by p

# we have to remove the subarray that gives extrasum = totsum % p 

# we have to find the smallest subarray that gives remainder totSum % p

# here we keep track the remainders of the prefixSum 



class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        totSum = 0;
        for num in nums:
            totSum = (totSum + num) % p;
        
        target = totSum % p;
        if(target == 0):
            return 0;

        prefixMap = {0:-1};
        prefixSum = 0;
        minLen = len(nums);
        for i in range(len(nums)):
            prefixSum = (prefixSum + nums[i]) % p;
            need = (prefixSum - target + p) % p;
            if need in prefixMap:
                minLen = min(minLen,i - prefixMap[need]);
            prefixMap[prefixSum] = i;
        
        if(minLen == len(nums)):
            return -1;
        return minLen;