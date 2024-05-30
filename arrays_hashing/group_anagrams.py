'''
Problem:
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a 
different word or phrase, typically using all the original letters exactly once.
'''

'''
Logic:
For this problem, our goal is to group the words that are anagrams of each together. The trick behind this problem is to use a dictionary
that maps something to a list of the words that are anagrams. We will then return the values of the dictionary. The problem is what should we
use as the keys of the dictionary. One approach is to use the words sorted as the key, as anagrams when sorted will be the same. This solution
does work but is inefficent as sorting takes O(nlogn) time. A better solution is to use the count of each character in the word as the key.
We can store these counts in a list length 26, each index per letter. The time complexity of this solution is O(n * m). n being the length of
the list, m being the length of each word
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
    