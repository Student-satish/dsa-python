class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = [];
        prefixSum = 0;
        for bit in nums:
            prefixSum = prefixSum << 1;
            prefixSum += bit;
            if prefixSum % 5 == 0:
                res.append(True);
            else:
                res.append(False);
            prefixSum = prefixSum % 5;
        return res;