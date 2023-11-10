
import matplotlib.pyplot as plt

data_x = [1,2,3,4]
data_1 = [10,30,20,40]
data_s = [100,200,450,300]
#data_color = ['#ff0000', '#00ff00', '#0000ff', '#ff00ff']
data_color = range(len(data_x))

plt.scatter(data_x, data_1
            , s=data_s
            , c=data_color
            , cmap='jet'
            )
plt.colorbar()
plt.show()