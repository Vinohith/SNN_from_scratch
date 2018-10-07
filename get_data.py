# loading data into vector format

import numpy as np
import _pickle as pickle
import os
from struct import unpack
import gzip
import matplotlib.pyplot as plt

MNIST_data_path = '/home/vinohith/Spiking_Neural_Networks_MNIST'


def get_labeled_data(picklename, bTrain=True):

    """Read input-vector (image) and target class (label, 0-9) and return
       it as list of tuples.
    """
    if os.path.isfile('%s.pickle' % picklename):
        data = pickle.load(open('%s.pickle' % picklename, 'rb'))
        print('Loaded file')
    else:
        print('Creating file')
        # Open the image in read binary mode
        if bTrain:
            images = gzip.open(os.path.join(MNIST_data_path, 'train-images-idx3-ubyte.gz'), 'rb')
            labels = gzip.open(os.path.join(MNIST_data_path, 'train-labels-idx1-ubyte.gz'), 'rb')
        else:
            images = gzip.open(os.path.join(MNIST_data_path, 't10k-images-idx3-ubyte.gz'), 'rb')
            labels = gzip.open(os.path.join(MNIST_data_path, 't10k-labels-idx1-ubyte.gz'), 'rb')

        # Get metadata for images
        images.read(4)  # skip the magic_number
        number_of_images = unpack('>I', images.read(4))[0]
        rows = unpack('>I', images.read(4))[0]
        cols = unpack('>I', images.read(4))[0]
        # Get metadata for labels
        labels.read(4)  # skip the magic_number
        N = unpack('>I', labels.read(4))[0]

        if number_of_images != N:
            raise Exception('number of labels did not match the number of images')
        # Get the data
        x = np.zeros((N, rows, cols), dtype=np.uint8)  # Initialize numpy array
        y = np.zeros((N, 1), dtype=np.uint8)  # Initialize numpy array
        for i in range(N):
            if i % 1000 == 0:
                print("i: %i" % i)
            x[i] = [[unpack('>B', images.read(1))[0] for unused_col in range(cols)]  for unused_row in range(rows) ]
            y[i] = unpack('>B', labels.read(1))[0]

        data = {'x': x, 'y': y, 'rows': rows, 'cols': cols}
        pickle.dump(data, open("%s.pickle" % picklename, "wb"))
    return data


# training = get_labeled_data('train_data')
# print(type(training))
# print(training.keys)
# # for i in training.keys():
# #     print(i)
# print(np.shape(training['x']))
# print(np.shape(training['x'][0]))

# plt.imshow(training['x'][0])
# plt.show()
# print(training['y'][0])
# print(training['x'][0])