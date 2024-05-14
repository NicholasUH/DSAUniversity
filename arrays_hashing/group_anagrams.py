'''
Problem:
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a 
different word or phrase, typically using all the original letters exactly once.
'''

'''
Logic:
Use a dictionary to store the grouped anagrams.
To create the key, create a list length 26, and fill it with 0.
To fill in the list, iterate through each word and increase the count at the index of that character(a - 0, b - 1, c - 2).
Then append the word to the dictionary using the list as the key.
Return the values of the dictionary.
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        char_count_dict = collections.defaultdict(list)

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord("a")] += 1
            
            char_count_dict[tuple(count)].append(word)

        return char_count_dict.values()
    