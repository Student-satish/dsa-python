class Solution:
    def largestPrime(self, n: int) -> int:
        ans = 0;
        primeSum = 0;
        for i in range(2,n+1):
            isPrime = True;
            for j in range(2,int(i ** 0.5)+1):
                if i % j == 0:
                    isPrime = False;
                    break;

            if(isPrime):
                primeSum += i;

            if(primeSum > n):
                break;
            isPrime = True;
            for j in range(2,int(primeSum ** 0.5) + 1):
                if primeSum % j == 0:
                    isPrime = False;
                    break;

            if(isPrime and primeSum <= n):
                ans = primeSum;
        
        return ans;    
        