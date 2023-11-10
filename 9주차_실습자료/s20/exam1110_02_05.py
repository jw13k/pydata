import random

import matplotlib.pyplot as plt

data_x = []
data_1 = []
data_s = []

# x,1,s 의 값 랜덤, 랜덤 범위 1~100
for i in range(10000):
    data_x.append(random.randint(1, 100))
    data_1.append(random.randint(1, 100))
    data_s.append(random.randint(1, 10))

data_color = range(len(data_x))

plt.scatter(data_x, data_1
            , s=data_s
            , c=data_color
            , cmap='jet'
            , alpha=0.6
            )
plt.colorbar()
plt.show()