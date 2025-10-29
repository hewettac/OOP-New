import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


x = np.array(["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10"])
y = np.array([80, 100, 62, 76, 88, 74, 93, 87, 99, 71])

print(np.mean(y))
print(np.median(y))
print(np.std(y))

plt.xlabel("Courses")
plt.ylabel("Grades")

## line chart
plt.plot(x, y) ## line chart
plt.show()

## pie chart
mylabels = ["a1", "a2", "a3", "a4", "a5"]
y = [20, 14, 60, 1, 5]
plt.pie(y, labels=mylabels)
plt.show()

## next set - pie and line
x = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

print(np.mean(y))
print(np.median(y))
print(np.std(y))

plt.xlabel = "Year"
plt.ylabel = "Age"

plt.plot(x, y)
plt.show()

plt.pie(y, labels = x)
plt.show()

## scatter plot
plt.scatter(x, y)
plt.show()