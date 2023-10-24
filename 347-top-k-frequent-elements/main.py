from typing import List


# O(N log N) solution
class Sort:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = {}
        for num in nums:
            numMap[num] = numMap[num]+1 if num in numMap else 1

        topF = dict(sorted(numMap.items(), key=lambda item: item[1], reverse=True))
        return list(topF.keys())[:k]

# O(N) solution
class Bucket:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = {}
        for num in nums:
            numMap[num] = 1 + numMap.get(num, 0)

        freq = [[] for _ in range(len(nums)+1)]

        for n, c in numMap.items():
            freq[c].append(n)

        res = []

        for topK in reversed(freq):
            while len(res) < k and len(topK) > 0:
                res.append(topK.pop())
                if len(res) == k:
                    return res

        return []




print(Bucket().topKFrequent(nums=[1, 2], k=2))