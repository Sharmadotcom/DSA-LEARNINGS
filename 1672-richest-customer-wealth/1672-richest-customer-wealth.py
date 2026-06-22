class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest=0
        for customer in accounts:
            wealth=sum(customer)
            richest=max(richest,wealth)
        return richest
