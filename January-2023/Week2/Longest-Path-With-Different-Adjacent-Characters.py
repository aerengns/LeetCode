# Day 13
class Solution:
    def longestPath(self, parent: List[int], labels: str) -> int:
        graph = [-1] * len(parent)
        graph = [[] for x in graph]

        for i, p in enumerate(parent):
            if i != 0:
                graph[i].append(p)
                graph[p].append(i)


        res = 1
        def dfs(n):
            ind = ord(labels[n])-97
            max1 = max2 = 0
            for neigh in graph[n]:
                if neigh == parent[n]: continue
                path_length = dfs(neigh)
                if labels[neigh] != labels[n]:
                    if path_length > max1:
                        max2 = max1
                        max1 = path_length
                    elif path_length > max2:
                        max2 = path_length

            nonlocal res
            res = max(res, max1 + max2 + 1)
            return max1 + 1

        dfs(0)
        return res
