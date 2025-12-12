# naive approach


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if(s == goal):
            return True;
        
        n = len(s);
        for i in range(n - 1):
            if s[i+1:] + s[:i+1] == goal:
                return True;
        
        return False;



# kmp algorithm -> optimized approach


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if(len(s) != len(goal)):
            return False;

        doubledString = s + s;
        return self.kmpSearch(doubledString,goal);

    
    def kmpSearch(self,text:str,pattern:str) -> bool:
        lps = self.computeLps(pattern);
        textIdx = patternIdx = 0;
        textLen = len(text);
        patternLen = len(pattern);
        while textIdx < textLen:
            if(text[textIdx] == pattern[patternIdx]):
                textIdx += 1;
                patternIdx += 1;
                if patternIdx == patternLen:
                    return True;
            elif(patternIdx > 0):
                patternIdx = lps[patternIdx-1];
            else:
                textIdx+=1;
        return False;

    def computeLps(self,pattern:str) -> list:
        patternLen = len(pattern);
        lps = [0];
        idx = 1;
        length = 0;
        while idx < patternLen:
            if pattern[idx] == pattern[length]:
                length+=1;
                lps.append(length);
                idx += 1;
            elif length > 0:
                length = lps[length-1];
            else:
                lps.append(0);
                idx += 1;
        return lps;


# optimized approach 

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if(len(s) != len(goal)):
            return False;
        
        doubledString = s + s;
        return doubledString.find(goal) != -1;
        
        