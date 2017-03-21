import csv
import openpyxl
import os

root_path = os.path.dirname(os.path.abspath(__file__))

def read_csv(filename):
    with open(root_path + '/static/onlinetest/docs/' + filename) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            print(', '.join(row))

def write_db(filename):
    with open(root_path + '/static/onlinetest/docs/' + filename) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            print(', '.join(row))


def read_xl(filenename):
    wb = openpyxl.load_workbook(root_path + '/static/onlinetest/docs/' + filename)
    print(wb.get_sheet_names())
    sheet = wb.get_sheet_by_name('Sheet3')
    print(sheet.title)
    anotherSheet = wb.active
    ws = wb.worksheets[0]
    print(ws)

read_xl('file1.csv')

#read_csv('file1.csv')
