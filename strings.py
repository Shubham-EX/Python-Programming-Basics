#Cerating
String = 'Shubham is here'
String1 = "Hello i am shubham"

print(len(String))

print(String)
print("Type of String is :" , type(String))
print(String1)
print("Type of String1 is :" , type(String1))

    #Multiline String

print("""
      My name is Shubham , i am in CSE at adani University. The study is easy at last night fut college experinceis worst.
      my opinion is you definately diserve a better college batter than adani at least
      """)


#String Concatention

word1 = "Hello"
word2 = "Shubham"

#1
print(word1 + " " + word2)

#2
word1 += " "  + word2
print(word1)

#3
Strings = ["Hello" , "Shubham" , "How", "are" ,"you"]
print(" ".join(Strings))

#4 using f string
name = "Shubham"
age = 20

print(f"Hello {name} , Is your age is {age}?")


#5 using format string
name = "Shubham"
age = 20
print( "{} {}".format(name,age))

#6 using %s string
name = "Shubham"
age = 20

print( "%s %s" % (name , age ))


#Indexing (Start with 0 to n-1 for positiv and -1 to -n i9n reverse in nagetive) 

String = "Shubham"

print(String[1])
print(String[6])
print(String[-1])
print(String[-7])


# Slicing [ start : end : step]

Name = "shubham"

print(Name[0 : 4 : 2])
print(Name[::-1]) #using  for reverse string

print(Name[1 : 5 : 2])

great = " Hello my name is Shubham"
print(great[6:])


#other operation

num = 19
words = str(num)
print(type(words))

name = "shubham"
print(name.upper())

name = "SHUBHAM Prajapati"
print(name.lower())
print(name.title()) #First character of all words are capital
print(name.capitalize()) #First Charactore of whole is capital 

print(name.index("Prajapati"))


String= "     Shubh     "

print(String.strip())
print(String.lstrip())
print(String.rstrip())

print(name.replace("Prajapati", "Kumhar"))

print(min(name))
print(max(name))

name =["Shubham", "Prajapati"]
print(" ".join(name))




sentence = "Hello my name is shubham prajapati"

print(sentence.startswith("Hello"))
print(sentence.startswith("Shubham"))
print(sentence.endswith("prajapati"))
print(sentence.endswith("shubham"))
print(sentence.find("Hello"))
print(sentence.find("Hi"))

num = "2018"
print(num.isdigit())

num = "a2018"
print(num.isdigit())



name = "shubham"
print(name.isupper())
name = "shubham"
print(name.islower())
