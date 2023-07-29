# 2651. Calculate Delayed Arrival Time

class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        if arrivalTime + delayedTime <= 23:
            return arrivalTime + delayedTime
        else:
            tmp = arrivalTime + delayedTime
            while tmp >= 24:
                tmp -= 24
            return tmp
