# 

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
class UndergroundSystem:
    def __init__(self):
        self.ids = {}
        self.pairs = collections.defaultdict(int)
        self.freqs = collections.defaultdict(int)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.ids[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        strat_station, start_time = self.ids.pop(id)
        self.pairs[(strat_station, stationName)] += t - start_time
        self.freqs[(strat_station, stationName)] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.pairs[startStation, endStation] / self.freqs[startStation, endStation]
        