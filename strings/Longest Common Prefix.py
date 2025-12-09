# intuition
# when you sort the strings lexicographically strings which differ the most will move far apart and the strings which are similar will come close together
# after sorting we just compare first and last strings because because they differ most


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort();
        first = strs[0];
        last = strs[len(strs)-1];
        ans = "";
        for i in range(len(first)):
            if first[i] == last[i]:
                ans += first[i];
            else:
                break;
        return ans;