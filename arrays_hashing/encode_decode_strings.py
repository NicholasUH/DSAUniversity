'''
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode
'''

'''
Logic:
This problem asks us to create two functions, one to encode a string and one to decode the encoded string. The trick behind this problem
is finding a way to make sure that when decoding the string, we correctly guess where the word begins and ends. To solve this, when we encode
the list of strings together, we will add the length of the word in front of the word. We will also add a delimiter symbol as numbers could also
be apart of the words. The list of words should now be one string for decoding. Now when we decode the string, we will have two iterators, i and j,
which will help us to iterate through the string and find the length of the word and then find the word. The i iterator will always start
at the index that contains the length, and j will start at the next index. j will look for the delimiter symbol to know when to stop. The two 
iterators will then update to the begin and end of the word. For both functions, the time complexity is O(n) as we need to iterate through
the list of strings and the encoded string for each respective function.
'''

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for s in strs:
            encoded_string += str(len(s)) + "$" + s
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "$":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = j + length
            result.append(s[i:j+1])

            i = j + 1
        
        return result
        