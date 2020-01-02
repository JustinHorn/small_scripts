import os
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf 





# dataset variables

#Model variables
hidden_layer_size = 100
nodes = [27,hidden_layer_size,9]

def r_squared(y_true, y_pred):
    numerator = tf.math.reduce_sum(tf.math.square(y_true - y_pred))
    y_true_mean = tf.math.reduce_mean(y_true)
    denominator = tf.math.reduce_sum(tf.math.square(y_true - y_true_mean))
    r2 = tf.math.subtract(1.0, tf.math.divide(numerator, denominator))
    return r2#tf.clip_by_value(r2, clip_value_min=0.0, clip_value_max=1.0)

class Model():
    def __init__(self,actFunc=tf.nn.sigmoid):
        #Weights (Matrices)
        self.actFunc =actFunc
        self.layer_weights=[]
        self.bias_weights=[]
        l_n = len(nodes)
        for index, node in enumerate(nodes,start=0):
            if index+1 < l_n:
                self.layer_weights.append(tf.Variable(tf.random.uniform(shape =[node,nodes[index+1]],minval=-2.0,maxval=2.0),name="W"+str(index)))
                self.bias_weights.append(tf.Variable(tf.constant(0.0,shape=[nodes[index+1]]),name="b"+str(index)))

        self.variables = []

        for w in self.layer_weights:
            self.variables.append(w)
        for b in self.bias_weights:
            self.variables.append(b)

        self.learning_rate = 0.001
        self.optimizer = tf.optimizers.RMSprop(learning_rate=self.learning_rate) #SGD < Adam > RMSprop
        self.current_loss_val = None

    def get_variables(self):
        return {var.name: var.numpy() for var in self.variables}

    def predict(self,x):
        activation = x
        for i,l_weight in enumerate(self.layer_weights):
            neuron_inputs = tf.math.add(tf.linalg.matmul(activation,l_weight),self.bias_weights[i])
            activation = self.actFunc(neuron_inputs)
        return activation   

    def loss(self,y_true,y_pred): # cant be be done the old way
        loss_fn = tf.math.reduce_mean(tf.losses.mean_squared_error(y_true,y_pred))#1/N*Sum
        self.current_loss_val = loss_fn.numpy()
        return loss_fn

    def fit(self,x_train,y_train,epochs=10,show_all=1): # cant be done the old way
       # print("Weights at the start", self.get_variables())     

        for epoch in range(epochs):
            train_loss = self.update_variables(x_train,y_train).numpy()
            train_r2 = self.compute_metrics(x_train,y_train).numpy()
            if epoch % show_all == 0:
                print("Epoche: ", epoch,"of", epochs, 
                " - Train Loss: ", round(train_loss,4),
                " - Train R2: ", round(train_r2,4))
       # print("Weights at the end: ", self.get_variables())

    def update_variables(self, x_train,y_train):
        with tf.GradientTape() as tape:
            y_pred = self.predict(x_train)
            loss = self.loss(y_train, y_pred)
        gradients = tape.gradient(loss, self.variables)
        self.optimizer.apply_gradients(zip(gradients,self.variables))   
        return loss

    def evaluate(self, x, y):
        loss = self.loss(self.predict(x), y).numpy()
        r2 = self.compute_metrics(x,y).numpy()
        print("Loss: ", round(loss,4), " R2: ", round(r2,4)) 

    def compute_metrics(self,x,y):
        y_pred = self.predict(x)    
        return r_squared(y,y_pred)