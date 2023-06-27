# 682. Baseball Game

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        points = []
        for i in range(len(operations)):
            try:
                points.append(int(operations[i]))
            except:
                if operations[i] == '+':
                    points.append(points[-2]+points[-1])
                elif operations[i] == 'D':
                    points.append(points[-1]*2)
                else:
                    points = points[:-1]
        return sum(points)
