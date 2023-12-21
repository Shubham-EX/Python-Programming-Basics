#Arithmetic

a = 10
b = 20

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print("--",a//b)
print(2**3)

#assignemnet 

a = 10 
b = 20

a+=b
print(a)

a-=b
print(a)

a*=b
print(a)

#Comparision

a = 10
b = 20

print(a==b)
print(a>b)
print(a<b)

#logical

#Num = int(input("Enter A Num :"))
Num = 3
if Num > 10 or Num == 3 :
    print("Num is between 10-30 ..")
elif Num >30 and Num <50:
    print("Num is between 30-50")
else :
    print("Num is gretter than 50 ") 
    

#Membership Operation

list = [1,2,3,4]

print( 3 in list)
print( 5 in list)
print( 5 not in list)

name = "shubham"

print("s" in name)

#indentity 
a = [1,2,3]
b = [1,2,3]

print(a is b)
print(a is not b)



print(a == b)