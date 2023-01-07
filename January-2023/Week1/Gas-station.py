# Day 7
import numpy as np
class Solution:
    def canCompleteCircuit(self, gasses: List[int], costs: List[int]) -> int:
        if sum(gasses)-sum(costs)<0:
            return -1
        gas_arr, cost_arr = np.array(gasses), np.array(costs)
        arr = gas_arr - cost_arr
        current_gas = 0
        ans = 10**5 +1
        for i, dif in enumerate(arr):
            current_gas+=dif
            if current_gas<0:
                current_gas=0
                ans = 10**5 +1
            else:
                ans = min(i, ans)
        return ans
