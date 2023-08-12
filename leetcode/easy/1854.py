# 1854. Maximum Population Year

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        ctr, most = 0, 0
        years = {}
        for i in range(len(logs)):
            if logs[i][0] in years.keys():
                continue
            for j in range(len(logs)):
                if logs[j][0] <= logs[i][0] and logs[j][1] > logs[i][0]:
                    try:
                        years[logs[i][0]] += 1
                    except KeyError:
                        years[logs[i][0]] = 1
        sorted_years = dict(sorted(years.items(), key=lambda x: x[1]))
        
        max_pop = list(sorted_years.items())[-1][1]
        min_year = list(sorted_years.items())[-1][0]
        for year in list(sorted_years.items())[::-1]:
            if year[1] == max_pop and year[0] < min_year:
                min_year = year[0]
            elif year[1] == max_pop:
                continue
            else:
                break

        return min_year
