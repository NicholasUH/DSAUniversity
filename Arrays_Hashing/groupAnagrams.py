class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        create a hashmap to store sorted_word:anagrams
        store each word by the sorted version
        return the list of values
        '''
        hashmap = collections.defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word))
            hashmap[sorted_word].append(word)
        
        return list(hashmap.values())