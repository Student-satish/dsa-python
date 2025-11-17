class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        dist = -1;
        for i in  range(len(nums)):
            if(nums[i] == 0):
                if(dist != -1):
                    dist += 1;
            else:
                if(dist == -1 or dist >= k):
                    dist = 0;
                    continue;
                
                return False;
        
        return True;