# 1672. Richest Customer Wealth

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for customer in accounts:
            if sum(customer) > max_wealth:
                max_wealth = sum(customer)
        return max_wealth
