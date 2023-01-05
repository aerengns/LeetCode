# Day 1
class Solution:
    def wordPattern(self, pattern: str, string: str) -> bool:
        dic = dict()
        pattern = [x for x in pattern]
        string = string.split()
        if len(pattern) != len(string): return False
        for i, s in enumerate(string):
            try:
                if pattern[i] != dic[s]:
                    return False
            except KeyError:
                if pattern[i] in dic.values():
                    return False
                dic[s] = pattern[i]
        return True

