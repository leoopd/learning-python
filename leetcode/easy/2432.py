# 2432. The Employee That Worked on the Longest Task

class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        longest_task = logs[0][1]
        busiest_employee = logs[0][0]
        for i in range(len(logs)-1):
            if logs[i+1][1]-logs[i][1] > longest_task:
                longest_task = logs[i+1][1]-logs[i][1]
                busiest_employee = logs[i+1][0]
            elif logs[i+1][1]-logs[i][1] == longest_task:
                if logs[i+1][0] < busiest_employee:
                    busiest_employee = logs[i+1][0]
        return busiest_employee
