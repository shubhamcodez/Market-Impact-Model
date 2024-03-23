import gzip
import struct

class TAQQuotesReader(object):
    '''
    This reader reads an entire compressed binary TAQ quotes file into memory,
    uncompresses it, and gives its clients access to the contents of the file
    via a set of get methods.
    '''


    def __init__(self, filePathName ):
        '''
        Do all of the heavy lifting here and give users getters for the
        results.
        '''
        self._filePathName = filePathName
        with gzip.open( self._filePathName, 'rb') as f:
            file_content = f.read()
            self._header = struct.unpack_from(">2i",file_content[0:8])
            
            # millis from midnight
            endI = 8 + ( 4 * self._header[1] )
            self._ts = struct.unpack_from( ( ">%di" % self._header[ 1 ] ), file_content[ 8:endI ] )
            startI = endI
            
            # bid size
            endI = endI + ( 4 * self._header[1] )
            self._bs = struct.unpack_from( ( ">%di" % self._header[ 1 ] ), file_content[ startI:endI ] )
            startI = endI

            # bid price
            endI = endI + ( 4 * self._header[1] )
            self._bp = struct.unpack_from( ( ">%df" % self._header[ 1 ] ), file_content[ startI:endI ] )
            startI = endI
            
            # ask size
            endI = endI + ( 4 * self._header[1] )
            self._as = struct.unpack_from( ( ">%di" % self._header[ 1 ] ), file_content[ startI:endI ] )
            startI = endI

            # ask price
            endI = endI + ( 4 * self._header[1] )
            self._ap = struct.unpack_from( ( ">%df" % self._header[ 1 ] ), file_content[ startI:endI ] )

    def getMillisFromMidn( self, index ):
        return self._ts[ index ]

    def getTimestamp(self, index ):
        return self.getMillisFromMidn( index )

    def getN(self):
        return self._header[1]
    
    def getSecsFromEpocToMidn(self):
        return self._header[0]
    
    def getMillisFromMidn( self, index ):
        return self._ts[ index ]

    def getAskSize( self, index ):
        return self._as[ index ]
    
    def getAskPrice( self, index ):
        return self._ap[ index ]

    def getBidSize( self, index ):
        return self._bs[ index ]
    
    def getBidPrice( self, index ):
        return self._bp[ index ]

    def getPrice(self, index):
        return (self.getAskPrice(index)+self.getBidPrice(index))/2
