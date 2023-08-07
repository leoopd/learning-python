# 1103. Distribute Candies to People

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0 for x in range(num_people)]
        ctr = 1
        while candies > 0:
            for i in range(len(res)):
                if ctr >= candies:
                    res[i] += candies
                    candies = 0
                    break
                res[i] += ctr
                candies -= ctr
                ctr += 1
        return res
