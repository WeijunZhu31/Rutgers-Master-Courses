# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 18:37:55 2020

@author: alizadeh
"""
#%%
# This file is an example of a tensorflow expression where the
# derivative is also calculted. 
import tensorflow as tf
print("Tensorflow version: {}".format(tf.__version__))
# import numpy as np

#%%
# Now create the gradient nodes:
with tf.GradientTape() as g:
    # Define the variables
    x1=tf.Variable(2,dtype=tf.float32,name="x1") 
    x2=tf.Variable(1,dtype=tf.float32, name="x2")
    # Define "tensors" from these variables by forming expressions and
    # using known and user defined functions
    y1=2*x1+tf.math.exp(x2)
    y2=x1+x2+tf.math.exp(2*x1+x2)
    
    z1=tf.math.log(y1+y2)+tf.math.cos(y1**2+y2**2)
    z2=y1*y2+y2*y2
    z3=2*y1+y1**2+y1**3
    
    f1=tf.cos(z1+z2)
    f2=tf.math.log(1+tf.sin(z1+z3))
    f=f1*f2

g = g.gradient(f,[x1,x2])
# display(g)
g1 = g[0].numpy()
g2 = g[1].numpy()

print("x1=", x1.numpy(), "x2=", x2.numpy())
print("y1=", y1.numpy(),"y2=", y2.numpy())
print("z1=", z1.numpy(), "z2=", z2.numpy(), "z3=", z3.numpy())
print("f1=", f1.numpy(), "f2=", f2.numpy())
print("g1=", g1, "g2=", g2)


#%%
"""
This Part derives from Tensorflow 1.x !!!! Tensorflow 2.x do not need to initialized !!!
"""
# init=tf.compat.v1.global_variables_initializer()  # prepare an init node
# with tf.compat.v1.Session() as sess:
#     #sess.run(init)
#     x1.initializer.run()
#     x2.initializer.run()
#     x1Val,x2Val=x1.eval(),x2.eval()

#     y1Val,y2Val,z1Val,z2Val,z3Val,f1Val,f2Val,fVal,g1Val,g2Val=sess.run([y1,y2,z1,z2,z3,f1,f2,f,g1,g2])
#     # y1Val,y2Val,z1Val,z2Val,z3Val=sess.run([y1,y2,z1,z2,z3])
#     # f1Val,f2Val=sess.run([f1,f2])
#     # g1Val,g2Val=sess.run([g1,g2])
    
#     print("x1=",x1Val,"x2=",x2Val)
#     print("y1=",y1Val,"y2=",y2Val)
#     print("z1=",z1Val,"z2=",z2Val,"z3=",z3Val)

#     print("f1=",f1Val,"f2=",f2Val)
#     print("g1 =",g1Val, "g2=",g2Val)
        
