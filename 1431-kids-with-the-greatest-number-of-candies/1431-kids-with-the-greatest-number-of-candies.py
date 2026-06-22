class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res=[]
        greatest=max(candies)
        for i in candies:
            if i+extraCandies>=greatest:
                res.append(True)
            elif i+extraCandies<greatest:
                res.append(False)
        return res
            
