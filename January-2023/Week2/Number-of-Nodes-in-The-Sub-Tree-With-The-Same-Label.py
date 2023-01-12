# Day 12
class Solution:
    def dfs(self,n, p, edges, labels, visited, res):
        count = [0] * 26 
        visited[n] = True
        for edge in edges[n]:
            if p == edge or visited[edge]: continue
            lst = self.dfs(edge, n, edges, labels, visited, res)
            for i, elem in enumerate(lst):
                count[i] += elem
        ind = ord(labels[n])-97
        count[ind] += 1
        res[n] = count[ind]
        return count


    def countSubTrees(self, n: int, edges_list: List[List[int]], labels: str) -> List[int]:
        edges = {}
        for a, b in edges_list:
            if a in edges:
                edges[a].append(b)
            else:
                edges[a] = [b]
            if b in edges:
                edges[b].append(a)
            else:
                edges[b] = [a]
        res = [0]  * n
        visited = [False] * n
        self.dfs(0, -1, edges, labels, visited, res)

        return res
