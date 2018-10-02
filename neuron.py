import numpy as np
import random
import matplotlib.pyplot as plt 


# refractory_time = 5   #neuron refractory time (minimum time between subsequent spikes)
# v_threshold = 25       #threshold voltage
# v_spike = 4           #spiking voltage
# v_ref = 0             #refrence voltage
# v_min = -1
# time = np.arange(0, 350) #simulation time

class neuron:

	def __init__(self):
		self.refractory_time = 5
		self.rest_time = -1
		self.v = 0

	def initial(self, th):
		self.v_threshold = th
		self.rest_time = -1
		self.v = 0

	def check(self):
		if self.v >= self.v_threshold:
			self.v = 0
			return 1
		elif self.v < 0:
			self.v = 0
			return 0
		else:
			return 0

	def inhibit(self):
		self.v = -200