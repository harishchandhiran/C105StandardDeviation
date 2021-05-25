import math
import csv

with open("data.csv",newline = "") as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]
#finding mean
def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total = total + float(x)
    mean = total/n
    return(mean)
#Squaring and getting the values
squared_list = []
for num in data:
    a = float(num)-mean(data)
    a = a**2
    squared_list.append(a)
#getting sum of squared list
sum = 0
for i in squared_list:
    sum = sum + i
#dividing the sum by total values
result = sum/(len(data)-1)
sd = math.sqrt(result)
print(sd)