
import matplotlib.pyplot as plt
import numpy as np


column_average = {1: 0.49999999999999994, 2: 0.6187499999999999, 3: 0.34687500000000004, 4: 0.37500000000000006, 5: 0.45624999999999993, 6: 0.5812499999999998, 7: 0.5843750000000001, 8: 0.4749999999999999, 9: 0.41874999999999996, 10: 0.3125, 11: 0.5249999999999999, 12: 0.321875, 13: 0.496875, 14: 
0.29375, 15: 0.521875, 16: 0.478125}
x = list(column_average.keys())
y = list(column_average.values())
array_x = np.array(column_average)
print(array_x)
plt.bar(x,y)
plt.xlabel("Columnas")
plt.ylabel("Valores")
plt.title("Promedios por Columnas")

plt.show()