class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        totalBottles = numBottles
        emptyBottles = 0

        while numBottles >= numExchange:
            emptyBottles = numBottles % numExchange
            numBottles = numBottles // numExchange

            totalBottles += numBottles
            numBottles += emptyBottles

        return totalBottles
        