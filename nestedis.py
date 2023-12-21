""" 
if condition1 :
    #statments
    if condition2 :
        #statments
    else:
        #statments
"""

x = input("Enter Your Gender G/B :")
y = int(input("Enter Your age :"))


if x == "G" :
    if y >= 21 :
        print("You can go for marraig ")
    else :
        print("You are note go for marriage until 21")
elif x =="B" :
    if y >= 18 :
        print("You can go for marraig ")
    else :
        print("You are note go for marriage until 18")
    