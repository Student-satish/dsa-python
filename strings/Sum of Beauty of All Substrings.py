class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s);
        ans = 0;
        for i in range(n):
            charCnt = {};
            for j in range(i,n):
                charCnt[s[j]] = charCnt.get(s[j],0) + 1;
                maxFreq , minFreq = 1 , n;
                for key in charCnt:
                    maxFreq = max(charCnt[key],maxFreq);
                    minFreq = min(charCnt[key],minFreq);
                ans += (maxFreq-minFreq);
        return ans;