class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n , m = len(s) , len(t);
        charMap1 = {};
        charMap2 = {};
        for i in range(m):
            if t[i] in charMap1:
                if charMap1[t[i]] != s[i]:
                    return False;
            charMap1[t[i]] = s[i];
            if s[i] in charMap2:
                if charMap2[s[i]] != t[i]:
                    return False;
            charMap2[s[i]] = t[i];
        return True;