# -*- coding: utf-8 -*-
"""
Title : Homework02-02
Created on Mon Mar 23 22:45:36 2020
@author: Weijun Zhu
"""
#%%
import tensorflow as tf
print("Tensorflow version: {}".format(tf.__version__))

#%%
# a). 
# f2: 
with tf.GradientTape() as gt:
    # Define the variables
    x = tf.Variable(1, dtype=tf.float32, name="x") 
    y = tf.Variable(1, dtype=tf.float32, name="y")
    z = tf.Variable(1, dtype=tf.float32, name="z")
        
    n1 = x*y
    n2 = n1*y
    n3 = tf.math.sigmoid(n1+y)
    n4 = 2*n3+x
    f2 = (tf.math.exp(n3))/(tf.math.exp(n1)+tf.math.exp(n3)+tf.math.exp(n4))

gt = gt.gradient(f2,[x,y,z])
gt1 = gt[0].numpy()
gt2 = gt[1].numpy()

print("f2 function: ")
print("x=", x.numpy(), "y=", y.numpy(), "z=", z.numpy())
print("n1=", n1.numpy(),"n2=", n2.numpy(), "n3=", n3.numpy(), "n4=", n4.numpy())
print("f2=", f2.numpy())
print("g1=", gt1, "g2=", gt2)

#%%
# The value of the gradient vector of f2
def gradient_value(g1, g2, g3):
    x = g1
    y = g2
    z = g3
        
    n1 = x*y
    n2 = n1*y
    n3 = tf.math.sigmoid(n1+y)
    n4 = 2*n3+x
    f2 = (tf.math.exp(n3))/(tf.math.exp(n1)+tf.math.exp(n3)+tf.math.exp(n4))
    return f2

print("The value of the gradient vector of f2 is: {}"\
      .format(gradient_value(gt1, gt2, g3=None)))

