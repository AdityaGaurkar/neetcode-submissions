from collections import defaultdict
from operator import itemgetter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1
        
        sorted_freq = sorted(freq.items(), key = itemgetter(1), reverse = True)
        result = []
        for num, count in sorted_freq[:k]:
            result.append(num)
        return result
        