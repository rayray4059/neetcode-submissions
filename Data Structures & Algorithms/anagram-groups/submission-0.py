class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            ordered = "".join(sorted(s))
            if ordered in anagrams:
                anagrams[ordered] = anagrams[ordered] + [s]
            else: 
                anagrams[ordered] = [s]
            
        return [i for i in anagrams.values()]
        

    

