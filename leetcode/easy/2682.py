# 2682. Find the Losers of the Circular Game

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        received = {x: False for x in list(range(1, n+1))}
        received[1] = True
        res = []
        i = 1
        ctr = 1
        while True:
            i += ctr*k
            while i > n:
                i -= n
            if received[i]:
                break
            else:
                received[i] = True
            ctr += 1

        for key in received.keys():
            if not received[key]:
                res.append(key)
        return res
