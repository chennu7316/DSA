class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        jew=set()
        for i in jewels:
            jew.add(i)
        count=0
        for i in stones:
            if i in jew:
                count+=1
        return count
