#line plot


import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1, 5, 7, 14]

plt.plot(x,y)

plt.xlabel("time")
plt.ylabel("done work")
plt.title("Works done in time")


plt.show()  

#scatter graph

x = [155,163,170,175,180]
y =[58,65,70,75,82]

plt.scatter(x,y)

plt.xlabel("x variabale")
plt.ylabel("y variabale")
plt.title("euations relation")

plt.show()

#pie chart

value = [ 21, 45,10]
marks = ["maths","SS","comp"]

plt.pie(value,labels=marks)

plt.title("10th marks ")

plt.show()

#bar chart

marks = ["maths","SS","comp"]
value = [ 21, 45,10]

plt.bar(marks,value)

plt.xlabel("marks")
plt.ylabel("value")
plt.title("10th marks ")

plt.show()