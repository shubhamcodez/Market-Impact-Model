from numpy import floor

class LastPriceBuckets(object):
    def __init__(
            self,
            data,  # Must implement getPrice(i), getTimestamp(i), and getN()
            numBuckets,
            startTS,  # eg 930AM = 19 * 60 * 60 * 1000 / 2
            endTS  # eg. 4PM = 16 * 60 * 60 * 10000
    ):
        # Save start and end times
        if startTS is None:
            startTS = 19 * 60 * 60 * 1000 / 2
        if endTS is None:
            endTS = 16 * 60 * 60 * 1000
        self._startTS = startTS
        self._endTS = endTS
        bucketLen = (endTS - startTS) / numBuckets

        # Initialize timestamp and price lists
        self._timestamps = [None] * numBuckets
        self._prices = [None] * numBuckets

        nRecs = data.getN()
        for startI in range(0, nRecs):
            timestamp = data.getTimestamp(startI)
            # Are we past the end of good data?
            if timestamp >= endTS:
                # Yes, we are past the end of good data
                # Stop computing data buckets
                break
            # Are we still iterating over data before the specified start?
            if timestamp < startTS:
                # Yes, we have to skip this data
                continue
            iBucket = int(floor((timestamp - startTS) / bucketLen))
            self._timestamps[iBucket] = timestamp
            self._prices[iBucket] = data.getPrice(startI)

    def getPrice(self, index):
        return self._prices[index]

    def getTimestamp(self, index):
        return self._timestamps[index]

    def getN(self):
        return len(self._prices)
