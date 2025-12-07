# for every primitive in string s we are keeping track of index of first opening bracket and index of last closing bracket

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        n = len(s);
        ans = "";
        stack = [];
        for i in range(n):
            if s[i] == '(':
                stack.append(i);
            else:
                if(len(stack) == 1):
                    ans += s[stack[0]+1:i];
                stack.pop();
        return ans;


# optimized approach
    class Solution:
        def removeOuterParentheses(self, s: str) -> str:
            ans = [];
            # whenever depth equal to zero we are starting new primitive
            depth = 0;
            for c in s:
                if c == '(':
                    if depth > 0:
                        ans.append("(");
                    depth += 1;
                else:
                    depth -= 1;
                    if depth > 0:
                        ans.append(")");
            
            return "".join(ans);