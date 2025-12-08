class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        n = len(nums);
        map = [];
        for num in nums:
            currEle = num;
            binRep = "";
            while currEle != 0:
                val = currEle % 2;
                binRep += str(val);
                currEle = currEle // 2;

            decRep = 0;
            for i in range(len(binRep) - 1 , -1,-1):
                decRep += (int(binRep[i]) * (2 ** (len(binRep) - i - 1)));

            map.append([num,decRep]);
        
        sorted_map = sorted(map,key=lambda x:(x[1],x[0]));
        ans = [];
        for item in sorted_map:
            ans.append(item[0]);
        return ans;