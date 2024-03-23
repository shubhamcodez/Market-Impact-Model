from impactUtils.FirstPriceBuckets import FirstPriceBuckets
from impactUtils.LastPriceBuckets import LastPriceBuckets


# This class will be used to build return buckets,
# e.g. 2 minute returns
class ReturnBuckets(object):

    def __init__(
        self,
        data,  # An object that implements getTimestamp(i), getPrice(i), getN()
        startTS,  # In milliseconds from midnight
        endTS,  # In milliseconds from midnight
        numBuckets  # Desired number of return buckets
    ):
        # Save start and end times
        if startTS is None:
            startTS = 19 * 60 * 60 * 1000 / 2
        if endTS is None:
            endTS = 16 * 60 * 60 * 1000
        self._startTS = startTS
        self._endTS = endTS

        # Initialize bucket to None
        self._startTimestamps = [None] * numBuckets
        self._endTimestamps = [None] * numBuckets
        self._returns = [None] * numBuckets

        # Iterate over buckets, computing and saving
        # each bucket's return and start/end timestamps
        firstPriceBuckets = FirstPriceBuckets(data, numBuckets, self._startTS, self._endTS)
        lastPriceBuckets = LastPriceBuckets(data, numBuckets, self._startTS, self._endTS)
        for i in range(0, firstPriceBuckets.getN()):
            startTimestamp = firstPriceBuckets.getTimestamp(i)
            endTimestamp = lastPriceBuckets.getTimestamp(i)
            startPrice = firstPriceBuckets.getPrice(i)
            endPrice = lastPriceBuckets.getPrice(i)
            if startTimestamp is None or endTimestamp is None:
                continue
            self._startTimestamps[i] = startTimestamp
            self._endTimestamps[i] = endTimestamp
            self._returns[i] = (endPrice / startPrice) - 1.0

    # Get start time stamp of bucket specified by
    # index.
    def getStartTimestamp(self, index):
        return self._startTimestamps[index]

    # Get end time stamp of bucket specified by
    # index.
    def getEndTimestamp(self, index):
        return self._endTimestamps[index]

    # Get the return of bucket specified by
    # index.
    def getReturn(self, index):
        return self._returns[index]

    # Get number of returns.
    def getN(self):
        return len(self._startTimestamps)
