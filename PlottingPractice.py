import matplotlib.pyplot as plt
import random as r

data = """x,y
0,5
1,5
2,4
3,1
4,8
5,7
6,3
7,3
8,5
9,2
10,5
11,4
12,4
13,1
14,6
"""

index = [int(x.split(",")[0]) for x in data.split()[1:]]
value = [int(x.split(",")[1]) for x in data.split()[1:]]

plt.plot(index, value, "ro-", linewidth = 1, label = "Math scores")
new_values = [x * r.uniform(-1.5,1.5) for x in value]
plt.plot(index, new_values, "bx-", linewidth = 1, label = "Verbal scores")

plt.xlabel("Year Index")
plt.ylabel("Score")
plt.title("State Exam Scores")

plt.legend(shadow = False, loc = "upper left")

plt.bar(index,value)
plt.bar(index,new_values)

plt.show()