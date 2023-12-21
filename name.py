name = input("Enter Your Name:")

print("Hello",name,"How Are You?") 

print("19","06","2003", sep="-") 
print("19","06","2003", sep="-", end="Is that true date?")

Que = input ("Write Yes/NO :")
if Que == "Yes" :
    print("Thank You for answering...")
else :
    print(" Write your true date :")
    day = int(input("enter a day no:" )) 
    Mounth = int(input("enter a Mounth no:" )) 
    year = int(input("enter a year no:" ))
    print("Your real BOD is ", day , Mounth , year , sep="-") 