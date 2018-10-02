import numpy as np


def threshold(train):
	#tu = np.shape(train[0])[0]
	tu = np.shape(train)[0]
	thresh = 0
	for i in range(tu):
		simul_active = sum(train[:, i])
		if simul_active > thresh:
			thresh = simul_active

	return (thresh / 3)