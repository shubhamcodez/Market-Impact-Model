# Implementation of tick test for classifying
# trades as either buyer (1) or seller (-1) initiated.
# Starting classification is undetermined (0).
class TickTest(object):

    # We need a tolerance to determine if price
    # has changed
    TOLERANCE = 0.00001

    def __init__(self):
        self.side = 0
        self.prevPrice = 0

    def classify(self, newPrice):
        if self.prevPrice != 0:
            if newPrice > (self.prevPrice + type(self).TOLERANCE):
                self.side = 1
            else:
                if newPrice < (self.prevPrice - type(self).TOLERANCE):
                    self.side = -1
        self.prevPrice = newPrice
        return self.side

    def classifyAll(self, data, startTimestamp, endTimestamp):
        # Allocate space for classifications
        classifications = [0] * data.getN()
        resultCounter = 0
        for i in range(0, data.getN()):
            if data.getTimestamp(i) < startTimestamp:
                continue
            if data.getTimestamp(i) >= endTimestamp:
                break
            classifications[resultCounter] = (data.getTimestamp(i), data.getPrice(i), self.classify(data.getPrice(i)))
            resultCounter = resultCounter + 1
        return classifications[0:resultCounter]
