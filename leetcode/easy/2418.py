# 2418. Sort the People

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        persons = {heights[i]: names[i] for i in range(len(names))}
        persons_sorted = dict(sorted(persons.items()))
        return list(persons_sorted.values())[::-1]
