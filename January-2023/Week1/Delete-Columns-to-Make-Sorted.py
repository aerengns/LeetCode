# Day 3
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        size = len(strs[0])
        res = 0
        for i in range(size):
            col = [st[i] for st in strs]
            for j in range(len(col)-1):
                if col[j] > col[j+1]:
                    res += 1
                    break
        return res

