class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split();
        ans = ''
        for i in range(len(words) - 1, -1 , -1):
            ans += words[i];
            if(i != 0):
                ans += " ";
        return ans;


class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split();
        return " ".join(words[::-1]);


# step - 1 remove the trailing spaces and leading spaces
# step - 2 using split method split the string based on spaces then you will get the list of words
# step - 3 we will iterate through the list from end and append each words to answer
# step - 4 return ans

# learning points 

# strip() is used to remove leading and trailing spaces in python
# split() is used to break a string into parts based on separator and it cuts the string wherever it finds separator and returns list of peices
# separator.join() is used to combine all elements as a string by putting separator between them



