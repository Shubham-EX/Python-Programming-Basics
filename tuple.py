t = (1,2,3)
print(t)
print(type(t))
print(len(t))

t = ("shubh",18)
print(t)

#asccesinfg using indexing and slicing which is same as list

print(t[1])
print(t[-1])
print(t[-1:])


#built in function

l = [1,2,3,4]

t = tuple(l)
print(t)

print(min(t))
print(max(t))
print(len(t))
print(sum(t))

#methods


print(t.count(1))

print(t.index(4))
print(sorted(t))
print(list(t))

#zip()

name = ("shubham","Viny")
age = (20,21)
zip = zip(name,age)

print(zip)
