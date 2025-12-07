# we have a given a number string

# we have to find largest odd number substring in a string

# if there is no odd number return empty substring




# approach - 1

# for every substring ending at index i we will check if it is odd or not by looking at last digit
# if any substring lastdigit is odd it might be possible answer
# as we keep finding odd digits as  we move right side we will get larger answer
class Solution:
    def largestOddNumber(self, num: str) -> str:
        currNum = "";
        ans = "";
        for c in num:
            currNum += c;
            lastDigit = int(currNum[len(currNum)-1]);
            if(lastDigit % 2 != 0):
                ans = currNum;
        return ans;



# approach - 2

# just do iteration from right side whenever we get first odd digit return string from start to current idx

class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1 , -1 , -1):
            val = int(num[i]);
            if(val % 2 != 0):
                return num[:i+1];
        return "";



