import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

%tensorflow_version 2.x
import tensorflow as tf
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import LearningRateScheduler
from tensorflow.keras import layers, Sequential

from sklearn.model_selection import train_test_split
import string

seed = 0
tf.random.set_seed(seed)
np.random.seed(seed)

ImageGen_coeff = 10
epochs_num = 40

path = '/content/gdrive/My Drive/Dacon/ComputerVision/'

path_train = path + 'train.csv'
path_test = path + 'test.csv'
path_submission = path + 'submission.csv'

device_name = tf.test.gpu_device_name()
if device_name != '/device:GPU:0':
    raise SystemError('GPU device not found')
print('Found GPU at: {}'.format(device_name))

###################################################################################################################################################
def read_data_to_dataframe(path):
    return pd.read_csv(path)

def image_view(pdSeries):
    pixels = np.array(pdSeries.iloc[3:].map(lambda x : float(x))).reshape((28,28))
    plt.rcParams['figure.figsize'] = [8, 8]
    plt.imshow(pixels)
    plt.title("Digit : " + str(pdSeries.iloc[1]) + "   Letter" + str(pdSeries.iloc[2]), fontsize = 15)
    plt.show()

def generate_letter_hash():
    letter_hash = dict(zip(string.ascii_uppercase, [[1 if i == j else 0 for j in range(26)] for i in range(26) ]))
    return letter_hash

def data_split(train_data):
    pix = train_data.iloc[:, 3:].applymap(lambda x : x/255.).values.reshape(-1, 28, 28, 1)                               #normalize 안했음
    fix = train_data.iloc[:, 1:3].values

    datagenerator = ImageDataGenerator(rotation_range=10, zoom_range=0.10, width_shift_range=0.1,
                                       height_shift_range=0.1)
    gen = datagenerator.flow(pix, fix, shuffle = False, batch_size = 32)
    pixel, fixed, batch_index, limit = [], [], 0, 64 * ImageGen_coeff
    while batch_index <= limit:
        try:
            data = gen.next()
            pixel += list(data[0])
            fixed += list(data[1])
            batch_index += 1
        except:
            print("ImageGeneratorError")
            break
    fixed = np.asarray(fixed)
    pixel = np.asarray(pixel)

    X_train_pixel, X_valid_pixel, fixed_train, fixed_valid = train_test_split(pixel, fixed, test_size=0.2,
                                                                              random_state=seed)

    Y_train = to_categorical(fixed_train[:, 0], 10)
    Y_valid = to_categorical(fixed_valid[:, 0], 10)

    letter_hash = generate_letter_hash()
    X_train_label = np.asarray([letter_hash[letter] for letter in fixed_train[:, 1]])
    X_valid_label = np.asarray([letter_hash[letter] for letter in fixed_valid[:, 1]])

    return X_train_label, X_train_pixel, Y_train, X_valid_label, X_valid_pixel, Y_valid

train_data = read_data_to_dataframe(path_train)
X_train_label, X_train_pixel, Y_train, X_valid_label, X_valid_pixel, Y_valid = data_split(train_data)
print(X_train_label.shape, X_train_pixel.shape, Y_train.shape, X_valid_label.shape, X_valid_pixel.shape, Y_valid.shape)
###################################################################################################################################################
def multi_input_cnn_dense_model_1():
    cnn_input = layers.Input(shape = (28, 28, 1))
    cnn_mid = layers.Conv2D(32, kernel_size = 3, activation='relu')(cnn_input)
    cnn_mid = layers.Conv2D(32, kernel_size = 3, activation='relu')(cnn_mid)
    cnn_mid = layers.Conv2D(32, kernel_size = 5, strides=2, padding='same', activation='relu')(cnn_mid)
    cnn_mid = layers.Dropout(0.4)(cnn_mid)
    cnn_mid = layers.Conv2D(64, kernel_size = 3, activation='relu')(cnn_mid)
    cnn_mid = layers.Conv2D(64, kernel_size = 3, activation='relu')(cnn_mid)
    cnn_mid = layers.Conv2D(64, kernel_size = 5, strides=2, padding='same', activation='relu')(cnn_mid)
    cnn_mid = layers.Dropout(0.4)(cnn_mid)
    cnn_mid = layers.Conv2D(128, kernel_size = 4, activation='relu')(cnn_mid)
    cnn_output = layers.Flatten()(cnn_mid)
    cnn_model = tf.keras.Model(inputs = cnn_input, outputs = cnn_output)

    dense_input = layers.Input(shape=(26,))
    dense_mid = layers.Dense(26,activation = 'relu')(dense_input)
    dense_mid = layers.Dense(20,activation = 'relu')(dense_mid)
    dense_output = layers.Dense(10, activation='sigmoid')(dense_mid)
    dense_model = tf.keras.Model(inputs = dense_input, outputs = dense_output)

    concatenated = layers.concatenate([cnn_model.output, dense_model.output])
    concatenated = layers.Dense(32, activation = 'relu')(concatenated)
    concatenated = layers.BatchNormalization()(concatenated)
    concat_output = layers.Dense(10, activation='softmax')(concatenated)
    concat_model = tf.keras.models.Model([cnn_input, dense_input],concat_output)

    return concat_model

def plot_history(history):
    plt.rcParams['figure.figsize'] = [14, 14]
    fig = plt.figure()
    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 2)
    ax3 = fig.add_subplot(2, 2, 3)
    ax4 = fig.add_subplot(2, 2, 4)

    ax1.plot(history.history['accuracy'])
    ax1.set_xlabel('epoch')
    ax1.set_ylabel('accuracy')

    ax2.plot(history.history['loss'])
    ax2.set_xlabel('epoch')
    ax2.set_ylabel('loss')

    ax3.plot(history.history['val_loss'])
    ax3.set_xlabel('epoch')
    ax3.set_ylabel('val_loss')

    ax4.plot(history.history['val_acc'])
    ax4.set_xlabel('epoch')
    ax4.set_ylabel('val_acc')

    plt.show()


def train_and_save_model(ModelName ,model, epochs_num):
    model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
    # print(model.summary())
    annealer = LearningRateScheduler(lambda x: 1e-3 * 0.95 ** x)
    with tf.device('/device:GPU:0'):
        history = model.fit([X_train_pixel, X_train_label], Y_train, epochs=epochs_num,
                            validation_data=([X_valid_pixel, X_valid_label], Y_valid), callbacks=[annealer], verbose=1)
    model.save(path + ModelName + '.h5')
    print(
        f"CNN: Epochs={epochs_num:d}, " +
        f"Train accuracy={max(history.history['accuracy']):.5f}, " +
        f"Validation accuracy={max(history.history['val_accuracy']):.5f}"
    )
    plot_history(history)


def test_result_submit(ModelName = 'Model1'):
    model = tf.keras.models.load_model(path + ModelName + '.h5')
    letter_hash = generate_letter_hash()
    test_data = read_data_to_dataframe(path_test)

    X_test_pixel = test_data.iloc[:, 2:].applymap(lambda x : x/255.).values.reshape(-1, 28, 28, 1)
    X_test_label = np.array([letter_hash[letter] for letter in test_data.iloc[:, 1]])

    predicted = model.predict([X_test_pixel, X_test_label])
    res = np.array([int(np.argmax(x)) for x in predicted])

    submission = read_data_to_dataframe(path_submission)
    submission.loc[:,'digit'] = res
    submission.to_csv(path+'submission_'+ModelName+'.csv',index = False)


model = multi_input_cnn_dense_model_1()
train_and_save_model('Model1', model, epochs_num)
test_result_submit(ModelName = 'Model1')

#####################################################################################################################################3
def generate_letter_embedding(epochs_num):
    letter_hash = generate_letter_hash()

    train_data = pd.read_csv(path_train)
    test_data = pd.read_csv(path_test)
    Y = np.concatenate((train_data.loc[:,2].map(lambda letter : letter_hash[letter]).values, test_data.loc[:,1].map(lambda letter : letter_hash[letter]).values), axis = 0)
    X = np.concatenate((train_data.iloc[:,3:].values, test_data.iloc[:,2:].values), axis = 0)

    em_input = layers.Input(shape=(28, 28, 1))
    em_mid = layers.Conv2D(32, kernel_size=3, activation='relu')(em_input)
    em_mid = layers.Conv2D(32, kernel_size=3, activation='relu')(em_mid)
    em_mid = layers.Conv2D(32, kernel_size=5, strides=2, padding='same', activation='relu')(em_mid)
    em_mid = layers.Dropout(0.4)(em_mid)
    em_mid = layers.Conv2D(64, kernel_size=3, activation='relu')(em_mid)
    em_mid = layers.Conv2D(64, kernel_size=3, activation='relu')(em_mid)
    em_mid = layers.Conv2D(64, kernel_size=5, strides=2, padding='same', activation='relu')(em_mid)
    em_mid = layers.Dropout(0.4)(em_mid)
    em_mid = layers.Conv2D(128, kernel_size=4, activation='relu')(em_mid)
    em_output = layers.Flatten()(em_mid)

    train_mid = layers.Dense(64, activation='relu')(em_output)
    train_mid = layers.Dense(64, activation='relu')(train_mid)
    train_mid = layers.Dense(32, activation='relu')(train_mid)
    train_out = layers.Dense(26, activation='relu')(train_mid)

    em_model = tf.keras.Model(inputs=em_input, outputs=em_output)
    training_model = tf.keras.Model(inputs=em_input, outputs=train_out)

    em_model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
    training_model

    annealer = LearningRateScheduler(lambda x: 1e-3 * 0.95 ** x)
    print('training for embedding model')
    with tf.device('/device:GPU:0'):
        history = training_model.fit(X, Y, epochs=epochs_num, callbacks=[annealer], verbose=1)
    print(
        f"CNN: Epochs={epochs_num:d}, " +
        f"Train accuracy={max(history.history['accuracy']):.5f}, " +
        f"Validation accuracy={max(history.history['val_accuracy']):.5f}"
    )
    plot_history(history)

    return em_model