import tensorflow as tf
import matplotlib as plt
import numpy as np
import itertools
import os
import sys

x_data = []
y_data = []

dataset_name=sys.argv[1]

dir_full_path='/cve/dataset/dataset_name/'
path= os.path.dirname(dir_full_path)
dir_list=os.listdir(path)

print("dataset_name = ",dataset_name)

for i in range(len(dir_list)):
    dir_path= os.path.join(path+"/"+dir_list[i])
    print('datapath = ',dir_path)    
        
    basename = os.path.basename(dir_path)
    print('basename = ',basename)

    if(basename == 'CWE78'):
        y=[1,0,0,0,0,0,0,0,0]
    elif(basename == 'CWE120'):
        y=[0,1,0,0,0,0,0,0,0]
    elif(basename == 'CWE126'):
        y=[0,0,1,0,0,0,0,0,0]
    elif(basename == 'CWE134'):
        y=[0,0,0,1,0,0,0,0,0]
    elif(basename == 'CWE190'):
        y=[0,0,0,0,1,0,0,0,0]
    elif(basename == 'CWE327'):
        y=[0,0,0,0,0,1,0,0,0]
    elif(basename == 'CWE377'):
        y=[0,0,0,0,0,0,1,0,0]
    elif(basename == 'CWE676'):
        y=[0,0,0,0,0,0,0,1,0]
    elif(basename == 'CWE785'):
        y=[0,0,0,0,0,0,0,0,1] 
    elif(basename == 'png'):
        continue
    print("Y = ",y)
     
    file_list=os.listdir(dir_path)

    for j in range(len(file_list)):
        data_path= os.path.join(dir_path+"/"+file_list[j])
        x=np.loadtxt(data_path,dtype=int)
        x_data.append(x)
        y_data.append(y)


# Create the model
X = tf.placeholder(tf.float32, [None, 9])
Y = tf.placeholder(tf.float32, [None, 9])

nb_classes=9

W = tf.Variable(tf.random_normal([9, nb_classes]))
b = tf.Variable(tf.random_normal([nb_classes]))

logits = tf.matmul(X,W)+b
hypothesis = tf.nn.softmax(logits)

cost_i = tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=Y)
cost = tf.reduce_mean(cost_i)

learning_rate=0.1
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

#set accuracy
prediction = tf.argmax(hypothesis,1)
correct_prediction = tf.equal(prediction, tf.argmax(Y,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

print ("Training")
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(23001):
        sess.run(optimizer, feed_dict={X: x_data, Y:y_data})
        if step%100 ==0:
            #print(step, sess.run(cost, feed_dict={X:x_data, Y:y_data}))
            loss, acc = sess.run([cost,accuracy],feed_dict={X:x_data, Y:y_data})
            print("Step: {:5}\tLoss: {:.3f}\tAcc: {:.2%}".format(step,loss,acc))
              
    #NEW DATA
    #NEW_DATA = sess.run(hypothesis, feed_dict={X: [[1,11,7,9]]})
    #print(NEW_DATA, sess.run(tf.argmax(NEW_DATA,1)))
   
    #Predict
   # pred = sess.run(prediction, feed_dict={X: x_data})
   # for p,y in zip(pred, list(itertools.chain(*y_data))):
    #    print("[{}] Prediction: {} True Y: {}".format(p == int(y),p,int(y)))

print ("done")

