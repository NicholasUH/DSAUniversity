'''
Problem:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
'''

'''
Logic:
To check if the strings are anagrams, we first check if the lengths are equal, meaning that it is possible for it to be an anagram. Once we check
we can create two dictionaries that will store the counts of each letter in the string and check whether or not the dictionaries are equal, if
they are equal this indicates that the strings are anagrams.
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
    