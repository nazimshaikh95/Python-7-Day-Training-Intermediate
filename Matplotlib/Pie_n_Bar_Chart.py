from numpy import loadtxt
from matplotlib.pyplot import pie
import matplotlib.pyplot as plt

year , profit = loadtxt('company-a-data.txt', unpack = True)

#Construct pie chart for representing Profit

#plt.pie(profit , labels=year)
#plt.show()


#Construct Bar Chart

#plt.bar(year, profit)
#plt.show()

#modified Bar Charts

#plt.bar(year, profit, fill=False,color='b', hatch='/')
#plt.show()

#plt.bar(year, profit, color='b', hatch='/')
#plt.bar(year, profit, fill=False, hatch='//')
#plt.bar(year, profit, fill=False, hatch='||')
plt.bar(year, profit, color='w', hatch='\\')
plt.show()
