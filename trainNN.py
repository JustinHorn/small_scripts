from model import *
from loadAndParseData import *

import pickle

model = Model()
model.predict
model.fit(inputVector,outputVector,10000,10)


with open('TTTnn.pkl', 'wb') as output:
    pickle.dump(model, output, pickle.HIGHEST_PROTOCOL)