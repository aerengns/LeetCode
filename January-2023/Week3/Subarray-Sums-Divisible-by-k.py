# Day 19 Solution
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pmod = res = 0
        groups = [0] * k
        groups[0] = 1

        for num in nums:
            pmod = (pmod + num%k + k) % k
            res += groups[pmod]
            groups[pmod] += 1

        return res

