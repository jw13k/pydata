
from exam1110_03 import get_data

filename = '2023 10월  교통카드 통계자료.csv'
result = get_data(filename)

#print(result['header'])
#print(result['data'])

data = result['data']

max_rate = 0

for line in data:
    print(line)
    val1 = line[4]
    val2 = line[6]
    if val2 != 0 and val1 > 10000:
        rate = val1/val2
        if rate > max_rate:
            max_rate = rate
            print(val1, val2, rate)

for line in data:
    print(line)