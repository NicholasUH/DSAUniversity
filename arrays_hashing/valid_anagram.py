'''
Problem:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
'''

'''
Logic:
Check if length of s and t are equal.
Create two dictionaries, one for s and one for t.
Iterate through s and add each character and its count to the s dictionary.
Check if the t dictionary is equal to the s dictionary.
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
    