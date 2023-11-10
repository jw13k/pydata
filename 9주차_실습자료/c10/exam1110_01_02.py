import math

import matplotlib.pyplot as plt
from c10.exam1110 import get_data, display_bar_chart

filename = '../2022_연령별인구현황.csv'
gender = '남성'
search_text = '서울'

data_male = get_data(filename, gender, search_text)
print(data_male)

gender = '여성'

data_female = get_data(filename, gender, search_text)
print(data_female)

data_len = len(data_male)

line_x = range(max(data_male))


data_size = []

for i in range(data_len):
    data_size.append( math.sqrt( data_male[i] + data_female[i] ))

plt.scatter(data_male, data_female
            , s=data_size
            , c=range(data_len)
            , cmap='jet'
            , alpha=0.6)
plt.plot(line_x, line_x, color='red')
plt.show()