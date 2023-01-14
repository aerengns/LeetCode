# Day 14
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        eq_table = {}
        abc = {}
        for i in range(26):
            abc[chr(i + 97)] = i
            eq_table[i] = i
        def update(n, x):
            c = eq_table[n]
            if c == x:
                return
            eq_table[n] = x
            update(c, x)
        def get_min(s):
            x = eq_table[s]
            if x == s or x == 0:
                return x
            return get_min(x)
        for a,b in zip(map(lambda x: ord(x)-97, s1), map(lambda x: ord(x)-97, s2)):
            x = min(a,b, eq_table[a], eq_table[b])
            update(a,x)
            update(b,x)
        
        res = ''
        for s in baseStr:
            s = ord(s) - 97
            res += chr(get_min(s) + 97)
        
        return res
