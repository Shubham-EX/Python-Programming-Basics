#Types of files
"""
1. Text files (.txt)
    Contain plain text and are human-readable.
    Common formats include .txt, .csv, and .html.
    
2. Binary files (.jpg, .gif, .png, .pdf)
    Contain binary data that is not human-readable.
    Common formats include .jpg, .gif, .png, .pdf, and .docx
"""

#Createing and Reading text data

""" Create a file
- using open() and 'w' 
- .write mathod

"""
with open('write a text file.txt','w') as file:
    file.write('This is a text file that I created using Python!')
    file.write("my name is shubham i am study in cse.")
    file.write("\n my name is viny i am study in cse.")

"""read a file
- using open() and 'r'
- .read method


"""
with open('write a text file.txt','r') as file:
    print(file.read())
    
    

#Reading and Writing Binary Files:

"""Writing binary file
-using open() and wb
- .write method

"""
with open('image.png','wb') as file:
    file.write('This is a binary file'.encode('utf-8'))

""" read
- using open() and rb
- .read method

"""
with open('image.png','rb') as file:
    print(file.read())


#Reading and Writing CSV Files:

"""write
- using open() and 'w'
- .write method
- newline='' argument 

    
"""
import csv 

data = [['name','age'],['shubham',18],['viny',18]]

with open('filecsv.csv','w', newline='') as file :
    writer = csv.writer(file)
    writer.writerows(data)
    
    
""" read
- using open() and 'r'
- .read method

"""
import csv 

with open('filecsv.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
    
    