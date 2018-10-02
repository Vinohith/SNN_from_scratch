import numpy as np
from parameters import param as pa

def stdp(t):

	if t > 0:
		return pa.A_plus * np.exp(-float(t) / pa.tau_plus)
	elif t <= 0:
		return -pa.A_minus * np.exp(float(t) / pa.tau_minus)


def update(w, del_w):

	if del_w < 0:
		return w + pa.sigma * del_w * (w - abs(pa.w_min))
	elif del_w > 0:
		return w + pa.sigma * del_w * (pa.w_max - w)