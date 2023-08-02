# 2073. Time Needed to Buy Tickets

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        target = tickets[k]
        left = len(tickets[:k+1])
        time = 0
        
        for customer in tickets[:k+1]:
            if customer < target:
                time += customer
            else:
                time += target
        
        if target == 1:
                    return time

        for customer in tickets[k+1:]:
            if customer < target:
                time += customer
            else:
                time += target-1

        return time
