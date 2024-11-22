class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = defaultdict(list)
        
        for word in strs:
            # ['a', 'e', 't'] -> "aet"
            key = ''.join(sorted(word))
            anagrams[key].append(word)

        return list(anagrams.values())       