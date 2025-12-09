class Solution:
    def totalScore(self, hp: int, damage: List[int], requirement: List[int]) -> int:
        n = len(damage);
        prefixSum = [0];
        for i in range(n):
            prefixSum.append(damage[i] + prefixSum[-1]);
        totScore = 0;
        for i in range(n):
            target = requirement[i] + prefixSum[i+1] - hp;
            low , high = 0 , i+1;
            while low <= high:
                mid = (low + high) // 2;
                if(prefixSum[mid] >= target):
                    high = mid - 1;
                else:
                    low = mid + 1;
            if(low <= i + 1):
                totScore += (i - low + 1);
                
        return totScore;