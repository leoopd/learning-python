# 1189. Maximum Number of Balloons

class Solution(object):
    def maxNumberOfBalloons(self, text):
        min1 = 1000000
        res = {'b':0,'a':0,'l':0,'o':0,'n':0}
        for letter in text:
            if letter in res.keys():
                res[letter] += 1

        if res['l'] == 1 or res['o'] == 1:
            return 0

        res['l'] = res['l']/2
        res['o'] = res['o']/2

        for letter in res:
            if res[letter] < min1:
                min1 = res[letter]

        return min1
