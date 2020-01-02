from secondModel import *
from loadAndParseData import *

import pickle

model = Model()
model.fit(inputVector,outputVector,5000,10)


with open('TTTnn.pkl', 'wb') as output:
    pickle.dump(model, output, pickle.HIGHEST_PROTOCOL)