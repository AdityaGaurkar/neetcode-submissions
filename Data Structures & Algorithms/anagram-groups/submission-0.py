from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            # Automatically creates a list if the key doesn't exist
            anagram_map[key].append(word)

            # Accessing values as a list of lists
        result = list(anagram_map.values())
        return result