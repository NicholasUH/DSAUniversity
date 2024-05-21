'''
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode
'''

'''
Encode Logic:
Iterate through strs and append the the length of the string and a delimiter symbol then the string itself.
'''

'''
Decode Logic:
Have 2 pointers i and j, i will be the beginning of what we extract while j is the end.
Iterate through the encoded string
-set j equal to i and iterate j until the delimiter is found
-the bounds of i and j will be the length of the string
- set i = j + 1, the start of the string
- set j = j + length of string, the end of the string
-append the string to result
set i to j + 1, the next number for the next string
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
        