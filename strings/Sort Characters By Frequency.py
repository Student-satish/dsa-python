from heapq import heapify;
from collections import Counter;
class Solution:
    def frequencySort(self, s: str) -> str:
        charFreqMap = Counter(s);

        pq = [(-freq,char) for char,freq in charFreqMap.items()];
        heapq.heapify(pq);

        ans = "";

        while pq:
             freq , char = heapq.heappop(pq);
             ans += char * -freq;
        return ans;



class Solution:
    def frequencySort(self, s: str) -> str:
        # count the frequency of each character in a string
        counter = {};
        for c in s:
            counter[c] = counter.get(c,0) + 1;
        
        pairs = [];
        for key in counter:
            pairs.append([key,counter[key]]);
        
        sortedPairs = sorted(pairs,key = lambda x:x[1],reverse=True);
        ans = "";
        for pair in sortedPairs:
            ans += pair[0] * pair[1];
        return ans;