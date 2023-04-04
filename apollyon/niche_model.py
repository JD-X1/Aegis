import pandas as pd
import numpy as np
from numpy.random import default_rng
rng = default_rng()
import matplotlib.pyplot as plt

def niche_model(S, beta):
	# sorted array of length = species number
	n = np.sort(rng.uniform(low = 0, high = 1, size = S))
	r = np.zeros(S)

	# set up alpha and beta params and loop through and add diet range values to r array
	aleph = 1
	b = beta
	for i in range(0,S):
		# random number generation from beta dist
		x = rng.beta(aleph, beta)
		r[i] = n[i]*x

	# Plotting Prey Range vs. Niche Value of each species
	#plt.plot(n,r)
	#plt.ylabel("Diet Range")
	#plt.xlabel("Niche Value")
	#plt.show()


	# center of the range of each consumer
	c = np.zeros(S)
	for i in range(0,S):
		c[i] = rng.uniform(low = r[i]/2, high = [n[i]])


	# Determine which prey every consumer eats?

	prey = []
	numprey = np.zeros(S)

	for i in range(0,S):
		# establish limits of niche range
		nmin = c[i]-(r[i]/2)
		nmax = c[i]+(r[i]/2)
		# determine which species fall between niche min/max
		prey1 = (n>nmin).nonzero()
		prey2 = (n<nmax).nonzero()
		prey.append(np.intersect1d(prey1,prey2))
		p_i = (prey[i]==i).nonzero()
		if len(prey[i]) > 0 and np.any(p_i):
			holder = prey[i]
			holder = np.delete(holder,p_i[0])
			prey[i] = holder
			numprey[i] = len(prey[i])
	#plt.plot(n,numprey)
	#plt.ylabel("Prey Count")
	#plt.xlabel("Niche Value")
	#plt.show()

	out_mat = np.zeros((S,S), dtype = int)

	for i in range(0,S):
		ones_vec = prey[i]
		if np.any(ones_vec):
			for j in ones_vec:
				out_mat[i,j] = 1
				out_mat[j,i] = 1


	return out_mat
