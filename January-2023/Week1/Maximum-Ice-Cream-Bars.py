# Day 6
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs = sorted(costs)
        count = 0
        for cost in costs:
            if coins - cost >= 0:
                count += 1
                coins -= cost
            else:
                break
        return count
