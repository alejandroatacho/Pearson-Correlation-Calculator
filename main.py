# Pearson Correlation Calculator
import math

x = [7,3,2]
y = [5,7,9]

# Calculate the mean of x and y
xMean = sum(x) / len(x)
yMean = sum(y) / len(y)

# Lists
xiXList = [i - xMean for i in x]
yiYList = [i - yMean for i in y]
xiXyiYList = [i * j for i, j in zip(xiXList, yiYList)]
xPowerList = [math.pow(i, 2) for i in xiXList]
yPowerList = [math.pow(i, 2) for i in yiYList]

# calculate correlation as r
r = sum(xiXyiYList) / math.sqrt(sum(xPowerList) * sum(yPowerList))

print(r)
