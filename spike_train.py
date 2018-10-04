import numpy as np 
from parameters import param as pa
import math

def encode(pot):

	train = []

	for l in range(pa.pix):
		for m in range(pa.pix):
			temp = np.zeros([(pa.T+1), ])
			freq = math.ceil(0.102*pot[l][m] + 52.02)
			freq1 = math.ceil(pa.pix / freq)
			k = freq1
			while k < pa.T:
				temp[k] = 1
				k = k + freq1
			train.append(temp)

	return train


# if __name__ == '__main__':
# 	pot = np.random.rand(28, 28)
# 	print(pot)
# 	train = encode(pot)
# 	print(np.shape(train))
# 	print(train)