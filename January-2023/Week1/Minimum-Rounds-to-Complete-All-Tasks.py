# Day 4
class Solution:
    def fillCounts(self, lst, size):
        for i in range(5, size):
            lst[i] = 1 + min(lst[i-3], lst[i-2])

    def minimumRounds(self, tasks: List[int]) -> int:
        task_dict = dict()
        max_count = 4
        for task in tasks:
            try:
                task_dict[task] += 1
                if task_dict[task] > max_count:
                    max_count = task_dict[task]
            except KeyError:
                task_dict[task] = 1
        round_count = 0
        count_list = [0] * (max_count +1)
        count_list[1], count_list[2],  count_list[3], count_list[4] = -1, 1, 1, 2
        max_count = 4
        print(task_dict)
        for key, value in task_dict.items():
            if value > max_count:
                self.fillCounts(count_list, value)
            c = count_list[value]
            print(count_list, c)
            if c < 1:
                return -1
            round_count += c
        return round_count
