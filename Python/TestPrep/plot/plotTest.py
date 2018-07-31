from matplotlib import pyplot
import random

x_values =[0, 4, 7, 20, 22, 25]

y_values = [random.randint(0, 30) for i in range(len(x_values))]
#y_values = [0, 2, 4, 6, 8, 10]
pyplot.plot (x_values, y_values, 'o-')
pyplot.ylabel('Values')
pyplot.xlabel('Time')
pyplot.title('Test plot')
pyplot.show()

print("hello")