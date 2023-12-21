l = [ 1,2,3]
l1 = ["shubham","viny","prince"]
print(l)
print(l1)
print(type(l))

mix = ["shubham",18 , 42.18,["Mehsana","Gujarat", ["gj" ,2]]]
print(mix)

# insdexing

print(mix[3][2][1])

name = ["shubham", "Prajapati", 18 , 2018 ,[19 , 2003]]

print(name[2])
print(name[-2])
print(name[-1][-1])

#slicing

name = ["shubham", "Prajapati", 18 , 2018 ,[19 , 6, 2003]]

print(name[1:3])
print(name[-1][0:3:2])
print(name[::-1])

# Built in Functiion 
L = [1,2,3,8,5]

print(len(L))
print(min(L))
print(max(L))
print(sum(L))\

#mathods
list = [ "red", "white","black"]
list.append("blue")
print(list)

list.remove("white")
print(list)

list.insert(1,"Meloni")
print(list)

list.append("red")
print(list)


print(list.index("red"))
print(list.count("red"))

list.reverse()
print(list)

L.sort()
print(L)

L.clear()
print(L)
