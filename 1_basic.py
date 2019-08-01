import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os

def environment_test():
    """
    Get information about your tensorflow version and also test gpu usage.
    :return:
    """
    print("Tensorflow Version: %s" % tf.__version__)
    print("GPU test: " + str(tf.test.is_gpu_available()))

def preprocess_data():
    """
    Download fashion mnist data and perform pre-processing
    :return:
    """
    # Download data
    fashion_mnist = tf.keras.datasets.fashion_mnist
    (x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
    x_train, x_test = x_train/255., x_test/255.

    # Preview
    img_show = np.concatenate([x_train[i] for i in range(10)], axis=1)
    plt.imshow(img_show, cmap='gray')
    plt.show()

    # Usual model takes 3 dimension image as input, (height, width, color channel)
    # Even though some datasets are gray scaled, it still needs color channel to be set as 1.
    x_train = x_train[..., tf.newaxis]
    x_test = x_test[..., tf.newaxis]
    print("Training dataset shape:" + str(x_train.shape) + ", " + "Validation dataset shape: " + str(x_test.shape))

    # 10000 here means the buffer size for shuffling.
    train_ds = tf.data.Dataset.from_tensor_slices(
        (x_train, y_train)).shuffle(10000).batch(32)
    test_ds = tf.data.Dataset.from_tensor_slices((x_test, y_test)).batch(32)

    return train_ds, test_ds


if __name__ == '__main__':
    environment_test()
    preprocess_data()