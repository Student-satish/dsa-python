# naive approach -> O(n^3)

class Solution:
    def checkPalindrome(self,s:str) -> bool:
        n = len(s);
        left , right = 0 , n - 1;
        while left < right:
            if s[left] != s[right]:
                return False;
            left += 1;
            right -= 1;
        
        return True;
    def longestPalindrome(self, s: str) -> str:
        n = len(s);
        ans = "";
        for i in range(n):
            currStr = "";
            for j in range(i,n):
                currStr += s[j];
                if self.checkPalindrome(currStr) and len(ans) < len(currStr):
                    ans = currStr;
        
        return ans;


# optimal approach(manachers algorithm) -> O(n^2)

class Solution:
    def oddLenPalindrome(self,s:str,index:int) -> str:
        n = len(s);
        left = index;
        right = index;
        while left >= 0 and right <= n - 1 and s[left] == s[right]:
            left -= 1;
            right += 1;
        left += 1;
        return s[left:right]
    def evenLenPalindrome(self,s:str,index:int) -> int:
        n = len(s);
        left = index;
        right = index + 1;
        while left >= 0 and right <= n - 1 and s[left] == s[right]:
            left -= 1;
            right += 1;
        left += 1;
        return s[left:right];
    def longestPalindrome(self, s: str) -> str:
        n = len(s);
        if n == 1:
            return s;
        ans = "";
        for i in range(n-1):
            oddLengthPalindrome = self.oddLenPalindrome(s,i);
            evenLengthPalindrome = self.evenLenPalindrome(s,i);
            if len(ans) < len(oddLengthPalindrome):
                ans = oddLengthPalindrome;
            if len(ans) < len(evenLengthPalindrome):
                ans = evenLengthPalindrome;
        
        return ans;
        


        

        

        