""" 
for var in sequence :
    statements
    
"""

# creatre a dictonory to entered number rith num and its square

x = int(input(" Enter a Number:"))

dict = {}

for i in range(1,x+1) :
    dict[i] = i**2
print(dict)



print("\n\nHear a table of this num")
for i in range(1,x+1) :
    print(x ,'*',i,"=",i*x)    
