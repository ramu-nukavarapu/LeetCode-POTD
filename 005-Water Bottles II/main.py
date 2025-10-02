class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        totalBottles = numBottles
        emptyBottles = numBottles
        numBottles = 0

        while numBottles != 0 or emptyBottles >= numExchange:
            if emptyBottles - numExchange >= 0:
                numBottles += 1
                emptyBottles -= numExchange
                numExchange += 1
            else:
                totalBottles += numBottles
                emptyBottles += numBottles
                numBottles = 0


        return totalBottles