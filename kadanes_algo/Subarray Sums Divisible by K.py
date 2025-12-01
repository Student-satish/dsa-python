class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        # if two prefixSums have same remainder then the subarray between them is divisible by k
        # if the remainder of the current prefixSum is occured some n times previously then it indicates there are n subarrays divisible by k ending at the current index
        n = len(nums);
        dict = {};
        prefixSum = 0;
        count = 0;
        dict[prefixSum] = 1;
        for num in nums:
            prefixSum += num;
            prefixSum %= k;
            count += dict.get(prefixSum,0);
            dict[prefixSum] = dict.get(prefixSum,0) + 1;
        return count;