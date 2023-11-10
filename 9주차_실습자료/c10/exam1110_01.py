
from c10.exam1110 import get_data, display_bar_chart



filename = '../2022_연령별인구현황.csv'
gender = '남성'
search_text = '전국'

data_male = get_data(filename, gender, search_text)
print(data_male)

gender = '여성'

data_female = get_data(filename, gender, search_text)
print(data_female)

#display_bar_chart('전국 성별', data_male, data_female)

m_data = []
f_data = []
data_size = len(data_male)

for i in range(data_size):
    m = data_male[i]
    f = data_female[i]
    if (m > f):
        m_data.append( m - f )
        f_data.append(0)
    else:
        f_data.append( f - m )
        m_data.append(0)

print()
print(m_data)
print(f_data)

display_bar_chart('전국 성별', m_data, f_data)
