import csv
import matplotlib.pyplot as plt

# gender: 남성, 여성
def get_data(filename):

    csv_file = open(filename, 'r', encoding='utf-8-sig')
    csv_data = csv.reader(csv_file)

    header = next(csv_data)
    data = []

    for line in csv_data:
        data.append(line)

    csv_file.close()

    return {
        'header' : header,
        'data' : data
    }

#end-def
