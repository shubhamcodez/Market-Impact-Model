# Class to calculate volume weighted average
# price for a given day of data between
# start timestamp and end timesamp,
# exclusive
class VWAP(object):
    def __init__(self, data, startTS, endTS):
        v = 0
        s = 0
        counter = 0
        for i in range(0, data.getN()):
            if data.getTimestamp(i) < startTS:
                continue
            if data.getTimestamp(i) >= endTS:
                break
            counter = counter + 1
            v = v + (data.getSize(i) * data.getPrice(i))
            s = s + data.getSize(i)
        if counter == 0:
            self.counter = 0
            self._vwap = 0
        else:
            self._counter = counter
            self._vwap = v / s

    def getVWAP(self):
        return self._vwap

    def getN(self):
        return self._counter
