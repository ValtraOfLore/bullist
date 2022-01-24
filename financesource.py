import csv
import yfinance

# Super class
class FinancialSource:
    pass

class YahooSource:
    def __init__(self):
        # To be moved to super class
        try:
            csvFile = open('Data/snp500.csv')
            reader = csv.reader(csvFile)
            asList = list(reader)
            self.TickerNames = [x[0] for x in asList]
            csvFile.close()
        except:
            csvFile.close()
            raise Exception('Cannot read file')
        

    def getTickerNames(self):
        return self.TickerNames

class GoogleSource:
    pass
    