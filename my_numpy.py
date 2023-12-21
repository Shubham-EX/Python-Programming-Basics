import numpy as np

#  create

arr = np.array([1,2,3,4,5,6])
print("1d array\n",arr)

arr2 = np.array([[1,2,3],[4,5,6]])
print("2d array\n",arr2)
             
zeroarr = np.zeros((3,3))
print("zero array\n",zeroarr)

onesarr = np.ones((2,2))
print("ones array\n",onesarr)

identityarr = np.eye(3)
print("identity array\n",identityarr)

rangearr = np.arange(0,10,2)
print("range array\n",rangearr)

linspacearr = np.linspace(1,5,4)
print("linspace array\n",linspacearr)

rand = np.random.rand(3,3)
print("random array\n",rand)



#Accessing

##indexing

arr = np.array([1,2,3,4,5,6])
print("\n\n\n",arr)

print("arr[2]:", arr[2])

arr2 = np.array([[1,2,3],[4,5,6]])
print("\n\n\n",arr2)

print("arr[1,2]:", arr2[1,2])

##slicing

arr = np.array([1,2,3,4,5,6])
print("\n\n\n",arr)

print("arr[2:5]:", arr[2:5])
print("arr[::-1]:", arr[::-1])
print("arr[0:4:2]:", arr[0:4:2])

arr2 = np.array([[1,2,3],[4,5,6]])
print("\n\n\n",arr2)

print("arr[1,:]:", arr2[1, :])
print("arr[:, 1:3]  :", arr2[:, 1:3]  )

# changing

arr = np.array([1,2,3,4,5,6])

arr[2] = 10
print("\n\n\n",arr)

arr2 = np.array([[1,2,3],[4,5,6]])

arr2[1,2] = 10
print("\n\n\n",arr2)


#Manipulating

##reshape
arr = np.array([1,2,3,4,5,6,7,8,9])
print("\n\n\nReshape(3x2)", arr.reshape(3,3))

##transposing
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("\n\n\nTransposr", arr.T)

##concatenating
arr = np.array([1,2,3])
arr2 = np.array([7,8,9])
print("\n\n\nConcatentation ")
print(np.concatenate((arr,arr2)))

##spliting
arr = np.array([1,2,3,4,5,6,7,8,9])
print("\n\n\nSpliting ", np.split(arr, 3))

##broadcasting
arr = np.array([1,2,3,4,5,6,7,8,9])
print("\n\n\nBroadcasting ", arr*2)


#Performing various operations

#arithmetic
###sum

arr = np.array([1,2,3])
arr2 = np.array([2,2,2])

print("sum",arr + arr2 )
###subtraction
print("subtraction",arr - arr2 )
###multiplication
print("multiplication",arr * arr2 )
###division
print("division",arr / arr2 )
###power
print("power",arr ** arr2 )

#aggregation 
###mean
arr = np.array([1,2,3,4,5,6,7,8,9])

print("mean",np.mean(arr))

###median
print("median",np.median(arr))

###standard deviation
print("standard deviation",np.std(arr))

###variance
print("variance",np.var(arr))

###max
print("max",np.max(arr))

###min
print("min",np.min(arr))

###argmax
#-give index of max
print("argmax",np.argmax(arr))

###argmin
#-give index of min
print("argmin",np.argmin(arr))


#mathematical

###sqrt
arr = np.array([1,2,3,4,5,6,7,8,9])
print("sqrt",np.sqrt(arr))

###log
print("log",np.log(arr))

###exp

print("exp",np.exp(arr))

###sin
print("sin",np.sin(arr))

###cos
print("cos",np.cos(arr))


#logical

arr = np.array([1,2,3,4,5,6,7,8,9])

###greater than

print("greater than",arr > 5)

###less than
print("less than", arr < 5)
###equal to
print("equal to", arr == 5)


#sort

arr = np.array([11,2,23,4,5,16,7,8,9])
print("sort",np.sort(arr))

#filter
arr = np.array([11,2,23,4,5,16,7,8,9])
print("filter",arr[arr>5])

