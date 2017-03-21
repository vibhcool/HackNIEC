import csv
import openpyxl
import os
from models import Users, studentProfile, question, quesFile, studentMark

root_path = os.path.dirname(os.path.abspath(__file__))

def file_to_db(filename):
    '''main function: write file to database'''
    if filename[:-3] == 'csv':
        read_csv(filename)
    elif filename[:-3] == 'xlsx' or filename[:-3] == 'xls':
        read_xl(filename)
    else:
        print('error')

def read_csv(filename):
    '''read csv file'''
    with open(root_path + '/static/onlinetest/docs/' + filename) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        data = {}
        data_row = []
        i = 0
        for row in spamreader:
            data[i] = {}
            j = 0
            data_row = row[0].split(',')
            for row_cell in data_row:
                data[i][j] = row_cell
                j += 1
            i += 1
    data['filename'] = filename
        #print(data)
    return data

    
def read_xl(filename):
    '''read excel file'''
    wb = openpyxl.load_workbook(root_path + '/static/onlinetest/docs/' + filename)
    print(wb.get_sheet_names())
    anotherSheet = wb.active
    ws = wb.worksheets[0]
    #print(ws.read())
    #total sheets
    data = {}
    for i in wb.worksheets:
        #all rows and columns
        row_count = i.max_row
        col_count = i.max_column
        print(row_count, col_count)
        for row in range(2,row_count):
            data[row-2] = {}
            for col in range(2,col_count):
                data[row-2][col-2] = i.cell(column=col, row=row).value
    data['filename'] = filename
    #print(data)
    return data

def write_db(data, client_name):
    '''write to database'''
    ques_paper=quesFile.objects.get(ques_paper_id=filename, client=client_name)
    for i in data:
        ques=question.objects.get(
            ques_paper_id=filename + '_' + data[i.key()].get(0),
            question=data.get(1),
            option1=data.get(2),
            option2=data.get(3),
            option3=data.get(4),
            option4=data.get(5),
            answer=data.get(6),
            questionType= data.get(7),
    )
        
#read_xl('quesformat.xlsx')

#write_db(read_csv('file1.csv'),'yoyo')

