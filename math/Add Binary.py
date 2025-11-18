class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m,n = len(a),len(b);
        i,j = m - 1 , n - 1;
        carry = 0;
        ans = "";
        while(i >= 0 or j >= 0 or carry == 1):
            val1 = 0;
            if i >= 0:
                val1 = int(a[i]);
                i -= 1;
            
            val2 = 0;
            
            if j >= 0:
                val2 = int(b[j]);
                j -= 1;
            
            val = val1 + val2 + carry;
            
            if(val == 0):
                ans += str(0);
                carry = 0;
            elif(val == 1):
                ans += str(1);
                carry = 0;
            elif(val == 2):
                ans += str(0);
                carry = 1;
            else:
                ans += str(1);
                carry = 1;
        return ans[::-1];