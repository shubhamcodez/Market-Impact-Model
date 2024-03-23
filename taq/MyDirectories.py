import gzip
import struct
import os

class MyDirectories:
    def __init__(self, root_path):
        self.root_path = root_path

    def getQuotesDir():
        # Assuming your quotes directory is located in the current working directory under 'quotes'
        return os.path.join("C:/Shubham/ATQSHW1/quotes")
        print("Here")
    def getTradesDir():
        # Assuming your quotes directory is located in the current working directory under 'quotes'
        return os.path.join('C:/Shubham/ATQSHW1/trades')