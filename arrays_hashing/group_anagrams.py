'''
Problem:
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a 
different word or phrase, typically using all the original letters exactly once.
'''

'''
Logic:
To group anagrams together, we will create a dictionary to store a key:list of anagrams.
The key that we will use will be tuple of character counts of each word. To create this tuple, we will create a list
of length 26, for a-z, then iterate through each word and add the character count of each word to a list.
We will then use the list as the key in the dictionary and add the word to the list associated with the key.
'''

'''
Psuedo-Code:
1.create a dictionary mapping character_counts : list of words
2. iterate through strs and repeat the steps
- calculate character count list using ascii values and indicies, a being index 0 to z being index 25
- add the word to the list associated with the character count
3.return dictionary values
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
    