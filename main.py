# Pearson Correlation Calculator
import math

x = [7,3,2]
y = [5,7,9]

# Calculate the mean of x and y
xSum = sum(x)
xMean = xSum / len(x)
ySum = sum(y)
yMean = ySum / len(y)
#Lists
xiXList = []
yiYList = []
xiXyiYList = []
xPowerList = []
yPowerList = []

for i in x:
    xiXcalc = i - xMean
    xiXList.append(xiXcalc)
    xPowerList.append(math.pow(xiXcalc,2))

for i in y:
    yiYcalc = i - yMean
    yiYList.append(yiYcalc)
    yPowerList.append(math.pow(yiYcalc,2))

for i, j in zip(xiXList, yiYList):
    xiXyiYcalc = i * j
    xiXyiYList.append(xiXyiYcalc)


# Pearson correlation calculation
r = sum(xiXyiYList) / math.sqrt(sum(xPowerList) * sum(yPowerList))

print(r)
