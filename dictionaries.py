dict = {"name": "Shubham", "age": 20}
print(dict)
print(type(dict))
print(len(dict))

#asseccing
print(dict["name"])

#adding

dict["address"] = "Mehsana"
print(dict)

#deleting
del dict["address"] 
print(dict)

dict["address"] = "Ambaliyasan"
print(dict)

#Built in function

print(dict.keys())
print(dict.values())
print(dict.items())


#Methods

dict1= {"Roll" : 18}

dict.update(dict1)
print(dict)


print(len(dict))

dict.clear()
print(dict)

print(dict.get("Gender",'N/A'))

print(dict)

