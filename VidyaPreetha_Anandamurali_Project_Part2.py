import sqlite3
import os
from contextlib import closing
from collections import defaultdict
import Vidyapreetha_Anandamurali_Project_Part1


class AbstractDAO(object):

    def __init__(self, name):
        self.name = name

    def insert_records(records):
        raise NotImplementedError

    def select_all(self):
        raise NotImplementedError

    def connect(self):
        #connect to the database identified by db_name
       return sqlite3.connect(self.name)

class BaseballStatsDAO(AbstractDAO):

    def insert_records(self, list123):
        print("Starting Baseball database insert. Please wait a few 'minutes' for the process to complete.....")
        connection2 = self.connect()
        cur2 = connection2.cursor()
        for row in list123:
            list = row.get()
            cur2.execute("INSERT INTO baseball_stats(player_name, salary, games_played, average) VALUES(?,?,?,?)",(list[0],list[1],list[2],list[3]))
            connection2.commit()
        print("Checking for Baseball Database completion")


    def select_all(self):
        connection3 = self.connect()
        cur3 = connection3.cursor()
        deque3 = cur3.execute("SELECT player_name, games_played, average, salary FROM baseball_stats")
        #deque3 = cur3.execute("SELECT player_name, games_played, average, salary FROM baseball_stats")

        print("Printing your Baseball Database select Query:")
        return deque3

    def select_all2(self):
        connection3 = self.connect()
        cur3 = connection3.cursor()
        deque3 = cur3.execute("SELECT average, salary FROM baseball_stats group by average")
        #deque3 = cur3.execute("SELECT average, salary FROM baseball_stats group by average")

        print("Printing your Baseball Database select Query:")
        return deque3


class StockStatsDAO(AbstractDAO):

    def insert_records(self, list456):
        print("Starting stocks database insert. Please wait a few 'minutes' for the process to complete.....")
        connection2 = self.connect()
        cur2 = connection2.cursor()
        for row in list456:
            list = row.get()
            cur2.execute("INSERT INTO stock_stats(company_name, ticker, country, price, exchange_rate, shares_outstanding, net_income, market_value, pe_ratio) VALUES(?,?,?,?,?,?,?,?,?)",(list[0],list[1],list[2],list[3],list[4],list[5],list[6],str(list[7]), str(list[8])))
            connection2.commit()
        print("Checking for Stocks Database completion")


    def select_all(self):
        connection3 = self.connect()
        cur3 = connection3.cursor()
        deque3 = cur3.execute("SELECT country, count(ticker) FROM stock_stats group by country")

        #deque3 = cur3.execute("SELECT company_name, ticker, country, price, exchange_rate, shares_outstanding, net_income, market_value, pe_ratio FROM stock_stats")
        print("Printing your stocks database select Query:")
        return deque3

    def select_all2(self):
        connection3 = self.connect()
        cur3 = connection3.cursor()
        #deque3 = cur3.execute("SELECT country, count(ticker) FROM stock_stats group by country")

        deque3 = cur3.execute("SELECT company_name, ticker, country, price, exchange_rate, shares_outstanding, net_income, market_value, pe_ratio FROM stock_stats")
        print("Printing your stocks database select Query:")
        return deque3


if __name__ == '__main__':
    #Main Method for stocks Database
    connection = sqlite3.connect('stocks.db')  # connection name is connection
    c = connection.cursor()  # cursor name is c
    print('Stocks Database created')
    connection.execute("CREATE TABLE IF NOT EXISTS stock_stats(company_name TEXT, ticker TEXT, country TEXT, price REAL, exchange_rate REAL, shares_outstanding REAL, net_income REAL,market_value REAL, pe_ratio REAL)")
    print("Stocks Table created, if it did not already exist")
    connection.commit()

    salaries = defaultdict(list)
    currDir = os.getcwd()
    fileSep = os.sep

    path = os.path.join(currDir + fileSep + fileSep + 'StockValuations.csv')
    stockreader = Vidyapreetha_Anandamurali_Project_Part1.StocksCSVReader(path) #Loading the csv file and its location
    list456 = stockreader.load() #The data to be stored in  our DB

    instance1 = StockStatsDAO('stocks.db')
    instance1.insert_records(list456)
    deque3 = instance1.select_all()
    for row in deque3:
        print(row)

    instance11 = StockStatsDAO('stocks.db')
    instance11.insert_records(list456)
    deque4 = instance11.select_all2()
    for row in deque4:
        print(row)
    connection.close()

    #########################################





    # Main Method for baseball Database
    connection2 = sqlite3.connect('baseball.db')  # connection2 name is connection
    c2 = connection2.cursor()  # cursor name is c
    print('Baseball Database created')
    connection2.execute("CREATE TABLE IF NOT EXISTS baseball_stats(player_name TEXT, salary INTEGER, games_played REAL, average REAL)")
    print("Baseball Table created, if it did not already exist")
    connection2.commit()

    salaries = defaultdict(list)
    currDir = os.getcwd()
    fileSep = os.sep

    path = os.path.join(currDir + fileSep + fileSep + 'MLB2008.csv')
    baseballReader = Vidyapreetha_Anandamurali_Project_Part1.BaseballCSVReader(path)
    list123 = baseballReader.load() #The data to be stored in  our DB

    instance2 = BaseballStatsDAO('baseball.db')
    instance2.insert_records(list123)
    deque4 = instance2.select_all()
    for row in deque4:
        print(row)


    instance22 = BaseballStatsDAO('baseball.db')
    instance22.insert_records(list123)
    deque44 = instance22.select_all2()
    for row in deque44:
        print(row)
    connection2.close()



