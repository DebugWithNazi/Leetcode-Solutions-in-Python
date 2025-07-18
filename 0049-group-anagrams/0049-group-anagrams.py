class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash_map = defaultdict(list)

        for string in strs:
            key = tuple(sorted(string))
            hash_map[key].append(string)
        
        return list(hash_map.values())
            



        