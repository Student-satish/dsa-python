class Solution:
    def cntSubstrs(self,s:str,k:int) -> int:
        n = len(s);
        uniqCharCnt = {};
        left = 0;
        cnt = 0;
        for right in range(n):
            uniqCharCnt[s[right]] = uniqCharCnt.get(s[right],0) + 1;
            while len(uniqCharCnt) > k:
                uniqCharCnt[s[left]] = uniqCharCnt[s[left]] - 1;
                if uniqCharCnt[s[left]] == 0:
                    uniqCharCnt.pop(s[left]);
                left+=1;
            
            cnt += right - left + 1;
        return cnt;
    def countSubstr (self, s, k):
        return self.cntSubstrs(s,k) - self.cntSubstrs(s,k-1);