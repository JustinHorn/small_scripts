import os
import numpy as np
#load
with open("trainData.txt","r") as o:
    data = o.read()

data = data.replace("\n","|||")
data = data.split("|||")
data = data[:-1] # remove last
#parse
inputVector, outputVector = [],[]

for index, vector in enumerate(data):
    if index%2==0:
        inputVector.append(vector)  
    else:
        outputVector.append(vector)

def changeString_toFloat(string):
    string= string.replace("(  ","|")
    string= string.replace("  )","")
    string = string[1:]
    string = string.replace(",",".")
    string = string.split("|")

    return string

inputVector = list(map(changeString_toFloat, inputVector) )
outputVector = list(map(changeString_toFloat, outputVector) )

inputVector = list(map(lambda x: [float(e) for e in x] ,inputVector) )
outputVector = list(map(lambda x: [float(e) for e in x], outputVector) )


inputVector = np.array(inputVector)
outputVector = np.array(outputVector)

inputVector = inputVector.astype(np.float32)
outputVector = outputVector.astype(np.float32)

print(inputVector.shape)
print(outputVector.shape)
print(inputVector[0].shape)
print(outputVector[0].shape)