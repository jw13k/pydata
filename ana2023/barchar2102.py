import csv

f = open('gendata.csv', encoding='utf-8')
data = csv.reader(f)

m = []
f = []
name = input('찾고 싶은 지역의 이름을 알려주세요 : ')
for row in data:
    if name in row[0]:
        for i in row[3:104]:
            m.append(-int(i.replace(',', '')))  # 쉼표 제거 후 정수로 변환
        for i in row[106:]:
            f.append(int(i.replace(',', '')))  # 쉼표 제거 후 정수로 변환

import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.figure(figsize=(10, 5), dpi=300)
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False
plt.title(name + ' 지역의 남녀 성별 인구 분포')
plt.barh(range(101), m, label='남성')
plt.barh(range(101), f, label='여성')
plt.legend()
plt.show()
