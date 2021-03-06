# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.callbacks import ModelCheckpoint
from keras.layers.normalization import BatchNormalization
import numpy as np


# Initialising the CNN
#classifier = Sequential()
model = Sequential()

# Step 1 - Convolution
#classifier.add(Conv2D(16, (3, 3), padding='same', activation='relu', input_shape=(256, 256, 3)))
#classifier.add(Conv2D(16, (3, 3), activation='relu'))
#classifier.add(MaxPooling2D(pool_size=(2, 2)))
#classifier.add(Dropout(0.25))

#classifier.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
#classifier.add(Conv2D(64, (3, 3), activation='relu'))
#classifier.add(MaxPooling2D(pool_size=(2, 2)))
#classifier.add(Dropout(0.25))

#classifier.add(Conv2D(32, (3, 3), padding='same', activation='relu'))
#classifier.add(Conv2D(32, (3, 3), activation='relu'))
#classifier.add(MaxPooling2D(pool_size=(2, 2)))
#classifier.add(Dropout(0.25))

#classifier.add(Flatten())
#classifier.add(Dense(512, activation='relu'))
#classifier.add(Dropout(0.5))
#classifier.add(Dense(9, activation='softmax'))

model.add(Conv2D(16, (3, 3), padding='same', use_bias=False, input_shape=(256, 256,3)))
model.add(BatchNormalization(axis=3, scale=False))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(4, 4), strides=(4, 4), padding='same'))
model.add(Dropout(0.25))

model.add(Conv2D(32, (3, 3), padding='same', use_bias=False))
model.add(BatchNormalization(axis=3, scale=False))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(4, 4), strides=(4, 4), padding='same'))
model.add(Dropout(0.25))

model.add(Conv2D(64, (3, 3), padding='same', use_bias=False))
model.add(BatchNormalization(axis=3, scale=False))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(4, 4), strides=(4, 4), padding='same'))
model.add(Dropout(0.25))

model.add(Conv2D(128, (3, 3), padding='same', use_bias=False))
model.add(BatchNormalization(axis=3, scale=False))
model.add(Activation("relu"))
model.add(Flatten())
model.add(Dropout(0.25))

model.add(Dense(512, activation='relu'))
model.add(Dense(9, activation='softmax'))
model.summary()

# Compiling the CNN
model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])


# Part 2 - Fitting the CNN to the images
from keras.preprocessing.image import ImageDataGenerator

# train_datagen = ImageDataGenerator(rescale = 1./255)

# 
train_datagen = ImageDataGenerator(rescale=1./255,
                                   rotation_range=10,
                                   shear_range=0.2,
                                   horizontal_flip=True,
                                   fill_mode='nearest',
                                   validation_split=0.33)

training_set = train_datagen.flow_from_directory('Juliet/C/testcases/cnt/png/',
                                                 shuffle=False,
                                                 seed=13,
                                                 target_size = (256, 256),
                                                 batch_size = 32,
                                                 class_mode = 'categorical',
                                                 subset="training")
validation_set = train_datagen.flow_from_directory('Juliet/C/testcases/cnt/png/',
                                                 shuffle=False,
                                                 seed=13,
                                                 target_size =(256, 256),
                                                 batch_size = 32,
                                                 class_mode = 'categorical',
                                                 subset="validation")

from keras.callbacks import CSVLogger

csv_logger = CSVLogger('./log.csv', append=True, separator=';')

hist = model.fit_generator(training_set,
                         steps_per_epoch = 1000,
                         epochs = 10,
                         validation_data = validation_set,
                         validation_steps = 10,
                         callbacks=[csv_logger])


from keras.models import load_model

model.save('cnn_attraction_keras_model.h5')

# output = classifier.predict_generator(test_set, steps=5)
# print(test_set.class_indices)
# print(output)

# 
print("-- Evaluate --")

scores = classifier.evaluate_generator(
            validation_set,
            steps = 10)

print("%s: %.2f%%" %(model.metrics_names[1], scores[1]*100))

# 
print("-- Predict --")

output = model.predict_generator(
            validation_set,
            steps = 10)
print(validation_set.class_indices)
np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})

print(output)
