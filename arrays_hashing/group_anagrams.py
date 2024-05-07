'''
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
    