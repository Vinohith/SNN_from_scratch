import numpy as numpy
from neuron import neuron
import random
from rec_field import receptive_field as rf 
from spike_train import encode
from stdp import stdp, update
from thresh import threshold
from parameters import param as pa 
import matplotlib.pyplot as plt
import os



pot_arrays = []
for i in range(pa.n):
	pot_arrays.append([])

time = np.arange(1, pa.T+1, 1)


layer2 = []

for i in range(pa.n):
	a = neuron
	layer2.append(a)


synapse = np.zeros((pa.n, pa.m))

for i in range(pa.n):
	for j in range(pa.m):
		synapse[i][j] = random.uniform(0, 0.4)


for k in range(pa.epoch):

	# print()
	# read the image (img)
	pot = rf(img)
	train = np.array(encode(pot))
	thresh = threshold(train)

	var_D = 0.15

	for x in layer2:
		x.initial(thresh)


	f_spike = 0
	img_win = 100 #??

	active_pot = []
	for index in range(pa.n):
		active_pot.append(0)


	for t in time:
		for j, x in enumerate(layer2):
			active = []
			if (x.rest_time < t):
				x.v = x.v + np.dot(synapse[j], train[:, t])
				if (x.v > pa.v_rest):
					x.v -= var_D
				active_pot[j] = x.v 
			pot_arrays[j].append(x.v)

		if(f_spike == 0):
			high_pot = max(active_pot)
			if (high_pot > thresh):
				f_spike = 1
				winner = np.argmax(active_pot)
				img_win = winner
				print('Winner is : {}'.format(winner))
				for s in range(pa.n):
					if (s != winner):
						layer2[s].v = pa.v_min

		for j, x in enumerate(layer2):
			s = x.check()
			if (s == 1):
				x.rest_time = t + x.refractory_time
				x.v = pa.v_rest
				for h in range(pa.m):
					for t1 in range(-2, pa.t_back-1, -1):
						if (0 <= t+t1 < pa.T+1):
							if (train[h][t+t1] == 1):
								synapse[j][h] = update(synapse[j][h], stdp(t1))

					for t1 in range(2, pa.t_fore+1, 1):
						if (0 <= t+t1 < pa.T+1):
							if (train[h][t+t1] == 1):
								synapse[j][h] = update(synapse[j][h], stdp(t1))


	if(img_win != 100):
		for p in rnage(pa.m):
			if sum(train[p]) == 0:
				synapse[img_win][p] -= 0.06
				if(synapse[img_win][p] < pa.w_min):
					synapse[img_win][p] = pa.w_min


ttt = np.arange(0, len(pot_arrays[0]), 1)
v_th = []
for i in range(len(ttt)):
	v_th.append(layer2[0].v_th)


