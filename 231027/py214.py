import csv

from exam2023 import get_data, display_chart
from exam2023 import get_data, display_bar_chart

filename = '2022_연령별인구현황.csv'

input_text = input('지역을 입력해 주세요.\n:')

data_2022_male =get_data(filename, '남성', input_text)
print(data_2022_male)

data_2022_female =get_data(filename, '여성', input_text)
print(data_2022_female)


filename = '2021_연령별인구현황.csv'

data_2021_male =get_data(filename, '남성', input_text)
print(data_2021_male)

data_2021_female =get_data(filename, '여성', input_text)
print(data_2021_female)

title = '2021년도/2022년도 남성 인구'

display_chart(title, data_2021_male, data_2022_male)
display_bar_chart(title, data_2021_male, data_2022_male)
