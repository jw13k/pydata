import matplotlib.pyplot as plt

x_data = [1, 2, 3, 4, 5]
y_data = [2, 4, 6, 8, 10]

plt.plot(x_data, y_data, marker='o', color='b', label='선 그래프')

plt.title('간단한 선 그래프 예제')

plt.xlabel('X 축')
plt.ylabel('Y 축')

plt.legend()

plt.grid(True)

plt.show()
