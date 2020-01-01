import os
import numpy as np
import tensorflow as tf 
from tensorflow.keras.utils import to_categorical


num_features = 18
num_classes = 9

nodes = [num_features,50,num_classes]
epochs = 50
print_all_x_epochs = 10

class Model():

    def __init__(self):
        self.layer_weights=[]
        self.bias_weights=[]
        for i in range(0,nodes.size)
            if i+1 < nodes.size:
                layer_weights.append(tf.Variable(tf.random.uniform(shape =[nodes[i],nodes[i+1]],minval=-2.0,maxval=2.0),name="W"+i))
                bias_weights.append(tf.Variable(tf.constant(0.0,shape=[nodes[i+1]]),name="b"+i))

        self.variables=[]
        for w in layer_weights:
            variables.append(w)

        for b in bias_weights:
            variables.append(b)

        self.learning_rate = 0.001        
        self.optimizer = tf.nn.optimizer.Adam(learning_rate=self.learning_rate)
        self.current_loss_value=False

    def update_variables(self, y_true,y_pred):
        with tf.GradientTape() as tape: #enter() exit()
            y_pred = self.predict(x_train)
            loss = self.loss(y_train, y_pred)
        gradients = tape.gradient(loss, self.update_variables)
        self.optimizer.apply_gradients(zip(gradients,self.variables))
        return loss

    def predict(self, x):
        activation = x
        for i in range(0,self.layer_weights.size):
            neuron_inputs = tf.math.add(tf.linalg.matmul(activation,layer_weights[i]),self.bias_weights[i])
            activation = tf.nn.sigmoid(neuron_inputs)
        return activation      

    def loss(self,x,y): # how many errors does our model make , mostly float
        loss_fn = tf.math.reduce_mean(tf.losses.mean_squared_error(y_true,y_pred))#1/N*Sum
        self.current_loss_val = loss_fn.numpy()
        return loss_fn

    def fit(self,x_train,y_train,epochs=100,all_x=1):

        for epoch in range(epochs):
            loss = update_variables(x_train,y_train).numpy()
            metric = compute_metric()
            if epoch % all_x == 0:
                print("Loss: ",loss," Metric: ",metric)

    def compute_metric(self, x,y):
        y_pred = self.predict(x)
        return r_squared(y,y_pred)      # how well does our modell Describe the test etc.      mostly integer


def r_squared(y_true, y_pred):
    numerator = tf.math.reduce_sum(tf.math.square(y_true - y_pred))
    y_true_mean = tf.math.reduce_mean(y_true)
    denominator = tf.math.reduce_sum(tf.math.square(y_true - y_true_mean))
    r2 = tf.math.subtract(1.0, tf.math.divide(numerator, denominator))
    return tf.clip_by_value(r2, clip_value_min=0.0, clip_value_max=1.0)   