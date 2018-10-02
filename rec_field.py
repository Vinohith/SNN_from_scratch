import numpy as numpy

def receptive_field(img):
	w = np.zeros([5,5])
	pot = np.zeros([28,28])
	ran = [-2,-1,0,1,2]
	ox = 2
	oy = 2
	w[ox][oy] = 1

	for i in range(5):
		for j in range(5):
			d = abs(ox-i) + abs(oy-j)
			w[i][j] = (-0.375)*d + 1

	for i in range(28):
		for j in range(28):
			summ = 0
			for m in ran:
				for n in ran:
					if (i+m)>=0 and (i+m)<=27 and (j+n)>=0 and (j+n)<=27:
						summ = summ + w[ox+m][oy+n]*img[i+m][j+n]
			pot[i][j] = summ

	return pot