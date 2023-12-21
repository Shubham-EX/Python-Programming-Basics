""" 
if codition1 :
    statement1
elif condition2 :
    statement2
elif condition3 :
    statement3
else:
    statement4
"""


x = int(input("enter a age :"))

if x >= 18 and x<= 40 :
    print(" adult ")

elif x >=13 and x < 18  :
    print("teen")
    
elif x >= 5 and x < 13 :
    print("child")
    
else :
    print("garda")