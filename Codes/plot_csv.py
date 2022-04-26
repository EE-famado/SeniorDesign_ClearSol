import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('data.csv', 'r') as csvfile:
        lines = csv.reader(csvfile, delimiter = ',')
        for row in lines:
            x.append(row[0])
            y.append(float(row[1]))
           

plt.plot(x, y, color = 'g', linestyle = 'dashed', marker = 'o', label = "CSV")
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.grid()
plt.show()