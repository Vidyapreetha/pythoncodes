import os
import csv
import sqlite3

class AbstractRecord(object):

    def __init__(self, name):
        self.name = name

class BaseballStatRecord(AbstractRecord):

    def __init__(self, player_name, salary, games_played, batting_average):
        self.player_name = player_name
        self.salary = salary
        self.games_played = games_played
        self.batting_average = batting_average

    def get(self):
        list_temp = [self.player_name, self.salary, self.games_played, self.batting_average]
        return list_temp

    def __str__(self):
        list_temp = [self.player_name, self.salary, self.games_played, self.batting_average]
        return ",".join(list_temp )

class StockStatRecord(AbstractRecord):

    def __init__(self, ticker, company_name, exchange_country, price, exchange_rate, shares_outstanding, net_income, market_value_usd, pe_ratio):
        self.ticker = ticker
        self.company_name = company_name
        self.exchange_country = exchange_country
        self.price = price
        self.exchange_rate = exchange_rate
        self.shares_outstanding = shares_outstanding
        self.net_income = net_income
        self.market_value_usd = market_value_usd
        self.pe_ratio = pe_ratio

    def get(self):
        list_temp = [self.ticker, self.company_name, self.exchange_country, self.price, self.exchange_rate, self.shares_outstanding, self.net_income, self.market_value_usd, self.pe_ratio]
        return list_temp

    def __str__(self):
        list_temp = [self.ticker, self.company_name, self.exchange_country, self.price, self.exchange_rate, self.shares_outstanding, self.net_income, str(self.market_value_usd), str(self.pe_ratio)]
        return",".join(list_temp )


class AbstractCSVReader():

    list_records = []

    def __init__(self, path):
        self.path = path

    def row_to_record(self, row):
        raise NotImplementedError

    def load(self):
        with open(self.path, mode='r') as cfile:
            csvfilereader = csv.reader(cfile)

            next(csvfilereader, None) # skip the headers
            for row in csvfilereader:
                record = self.row_to_record(row)
                self.list_records.append(record)
            return self.list_records

class BaseballCSVReader(AbstractCSVReader):

    def row_to_record(self, row):

        # validation
        try:
            if row == None:
                raise BadData()
        except ValueError:
            print("Value Error Occured")
        except ZeroDivisionError:
            print("Zero Division Occured")

        # parsing
        results_of_split = row

        newrecrd = BaseballStatRecord(results_of_split[0], results_of_split[2], results_of_split[6], results_of_split[68])

        # only return record not list
        return (newrecrd)

class StocksCSVReader(AbstractCSVReader):

    def float2(self, standard):
        if standard == '#DIV/0!':
            standard = 1
        else:
            try:
                standard = float(standard)
            except ValueError:
                standard = 1
        return standard

    def row_to_record(self, row):

        # validation
        try:
            if row == None:
                raise BadData()
        except ValueError:
            print("Value Error Occured")
        except ZeroDivisionError:
            print("Zero Division Occured")


        # parsing
        results_of_split = row


        self.market_value_usd  = self.float2(results_of_split[3]) * self.float2(results_of_split[4]) * self.float2(results_of_split[5])
        #results_of_split[3] * results_of_split[4] * results_of_split[5]#str(results_of_split[6])#float(results_of_split[3]) * float(results_of_split[4]) * float(results_of_split[5])

        self.pe_ratio =    self.float2(results_of_split[3]) * self.float2(results_of_split[5]) / self.float2(results_of_split[6])
        #str(results_of_split[6])

        newrecrd = StockStatRecord (results_of_split[0], results_of_split[2], results_of_split[1], results_of_split[3],results_of_split[4],results_of_split[5],results_of_split[6],self.market_value_usd, self.pe_ratio)

        # only return record not list
        return (newrecrd)



class BadData(ValueError):
    pass

'''
a.	load the CSV (e.g.  BaseballCSVReader('path to my CSV').load())
b.	Print each record to the console. You are to use: print(record)
'''

if __name__ == '__main__':

    ##Baseball Records
    currDir = os.getcwd()
    fileSep = os.sep

    path = os.path.join(currDir + fileSep + fileSep + 'MLB2008.csv')
    baseballReader = BaseballCSVReader(path)
    list123 = baseballReader.load()

    for abstract_record in list123:
        print (abstract_record)

    ##Stock Records

    path = os.path.join(currDir + fileSep + fileSep + 'StockValuations.csv')
    stockReader = StocksCSVReader(path)
    list789 = stockReader.load()
    for row in list789:
        print (row)
        
    print('Printed each of the 2 csv file records to the console as required')