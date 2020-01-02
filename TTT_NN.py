import os
import numpy as np
import tensorflow as tf 
from tensorflow.keras.utils import to_categorical


num_features = 27
num_classes = 9

nodes = [num_features,50,num_classes]
epochs = 50
print_all_x_epochs = 10

class Model():

    def __init__(self):
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
        self.optimizer = tf.optimizers.Adam(learning_rate=self.learning_rate)
        self.current_loss_value=False

    def update_variables(self,x,y_true):
        with tf.GradientTape() as tape: #enter() exit()
            y_pred = self.predict(x)
            loss = self.loss(y_pred,y_true)
        gradients = tape.gradient(loss, self.update_variables)
        self.optimizer.apply_gradients(zip(gradients,self.variables))
        return loss

    def predict(self, x):
        activation = x
        for i,l_weight in enumerate(self.layer_weights):
            neuron_inputs = tf.math.add(tf.linalg.matmul(activation,l_weight),self.bias_weights[i])
            activation = tf.nn.sigmoid(neuron_inputs)
        return activation      

    def loss(self,y_pred,y_true): # how many errors does our model make , mostly float
        loss_fn = tf.math.reduce_mean(tf.losses.mean_squared_error(y_true,y_pred))#1/N*Sum
        self.current_loss_val = loss_fn.numpy()
        return loss_fn

    def fit(self,x_train,y_train,epochs=100,all_x=1):

        for epoch in range(epochs):
            loss = self.update_variables(x_train,y_train).numpy()
            metric = self.compute_metric().numpy()
            if epoch % all_x == 0:
                print(epoch,"Loss: ",loss," Metric: ",metric)

    def compute_metric(self, x,y):
        y_pred = self.predict(x)
        return r_squared(y,y_pred)      # how well does our modell Describe the test etc.      mostly integer


def r_squared(y_true, y_pred):
    numerator = tf.math.reduce_sum(tf.math.square(y_true - y_pred))
    y_true_mean = tf.math.reduce_mean(y_true)
    denominator = tf.math.reduce_sum(tf.math.square(y_true - y_true_mean))
    r2 = tf.math.subtract(1.0, tf.math.divide(numerator, denominator))
    return tf.clip_by_value(r2, clip_value_min=0.0, clip_value_max=1.0)
