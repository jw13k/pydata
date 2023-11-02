import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [10, 25, 15, 30]

plt.figure(figsize=(8, 6))  
plt.bar(categories, values, color='skyblue') 


plt.title('Sample Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')


plt.show()
