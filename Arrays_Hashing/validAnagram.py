class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


        sMap, tMap = defaultdict(int), defaultdict(int)

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            sMap[s[i]] += 1
            tMap[t[i]] += 1
        
        
        return sMap == tMap

'''
1. create a two hashmaps that stores char:frequency
2. add string s and t to hashmaps
3. compare hashmaps to see if equal, if equal, then anagrams
'''