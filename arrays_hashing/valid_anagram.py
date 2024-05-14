'''
Problem:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
'''

'''
Logic:
We first check if the two strings are the same length as that is necessary for two strings to be an anagram. 
Then we will create two dictionaries for strings s and t. We will add the letters and their counts to the respective dictionaries. 
Next, we will check if the dictionaries are the same. If they are the same, it is an anagram.
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_dict = collections.defaultdict(int)
        t_dict = collections.defaultdict(int)

        for i in range(len(s)):
            s_dict[s[i]] += 1
            t_dict[t[i]] += 1

        return s_dict == t_dict
    