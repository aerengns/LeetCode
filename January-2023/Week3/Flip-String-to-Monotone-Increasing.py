# Day 17 Solution
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        if len(s) <= 1:
            return 0
        first_one = s.find('1')
        if first_one == -1:
            return 0
        counter = 0
        flips = 0
        for c in s[first_one:]:
            if c == '1':
                counter += 1
            else:
                flips += 1
            flips = min(flips, counter)
            
        return flips
