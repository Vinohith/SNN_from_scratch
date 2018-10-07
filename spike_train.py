import numpy as np 
from parameters import param as pa
import math

def encode(pot):

	train = []

	R = np.max(pot)
	print(R)
	for l in range(pa.pix):
		for m in range(pa.pix):
			temp = np.zeros([(pa.T+1), ])
			if pot[l][m] > 0:
				freq = 5 * (R / pot[l][m])
				k = freq
			elif pot[l][m] <= 0:
				k = 99999  #some very high value
			while k < pa.T:
				temp[int(k)] = 1
				k = k +freq
			train.append(temp)

	return train


# if __name__ == '__main__':
# 	pot = np.random.randn(28, 28)
# 	#print(pot)
# 	print(np.max(pot))
# 	print(np.min(pot))
# 	train = encode(pot)
# 	print(np.shape(train))
# 	ind = np.where(pot == np.max(pot))
# 	print(ind)
# 	#print(train)