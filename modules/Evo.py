#!usr/bin/python3
import os
import copy
import sys
import pandas as pd
import numpy as np
import scipy as sp

"""
	"And it came to pass in those days, as it had come before and would come
	again, that the Dark lay heavy on the land and weighed down the hearts
	of men, and the green things failed, and hope died...  Let the Prince of the
	Morning sing to the land that green things will grow and the valleys give
	forth lambs. Let the arm of the Lord of the Dawn shelter us from the
	Dark, and the great sword of justice defend us. Let the Dragon ride again
	on the winds of time."
	 - A Memory of Light, R. Jordan
"""

#### USER FLAG ACQUISITION ###
#def get_args():
#	None

class EvoSim(object):
	"""
	Base class for simulation

	############### Variables ##################
	- tmax(int64)       - maximum time steps
	- core_df(pd.df)    - df with core output

	###############  Methods   #################
	- time_step()       - moves simulation one
						  timestep forward
	- output_df()       - generates output at
						  current timestep

	##############  Subclasses  ##################
	- clock  - object tracks time steps and
			   interfaces with EvoEnv and EvoPop
			   to carry out operations needed to
	- EvoEnv - represents a kind of environment
			   generally a max of two should be
			   suffecient
	- EvoPop - represents populations


	"""
	tmax = 0
	def __init__(self, mode = "base"):
		if mode == "base":
			tmax = 100
			self.clock = time_piece("discrete", tmax)
			self.Env = EvoEnv(mode, name = "E1", tmax = tmax)
			self.Pop = EvoPop(mode, name = "P1", tmax = tmax, self.Env)
		elif mode == "usr":
			# args = get_args()
			TypeError("User Arg Mode In Development")
	def time_step(self):
		print("Starting Time:", self.clock.time)
		if self.clock.clock_type == "discrete":

		elif self.clock.clock_type == "continuous":
			RaiseError("continuous time version under development")

class time_piece(object):
	"""
	Intialize instance clock object tied to all environments
	and populations generated within the EvoEnv and EvoPop
	In concept
	"""
	def __init__(self, clock_type, tmax):
		self.timeType = clock_type
		if clock_type == "discrete":
			self.time = int(0)
		elif clock_type == "continuous":
			self.time = float(0.0)


class EvoPop(object):
	"""
	Base class for populations in simulation
	#################   Variables   ###################
	gen(int)		- counter for current generation
	n(array)		- array of len tmax, pop size
	 				  tracker per gen
	zBar(array)		- array of len tmax, avg z
					  per generation
	wBar(array)		- array of len tmax, avg W
					  per generation

	#################    Methods    ###################


	"""
	def __init__(self, mode="base", name="Pop", tmax=100, Env = None):
		"""
		Variables:
		gen(int)		- counter for current generation
		zBar(array)		- array of len tmax, avg z per generation
		n(int64) 		- population size
		popID(str)		- population string identifier
		Base Mode:
			- creates an instance of EvoPop that is designed to simulate
			one population
		"""

		if mode == "base":
			self.gen = 0
			self.sigma = 1.0
			self.zBar = np.zeros([tmax,], dtype=float) # empty float array of len = tmax tracks average pheno across time
			self.wBar = np.zeros([tmax,], dtype=float)
			self.n = np.zeros([tmax,], dtype=float)
			self.zBar[0] = random.Generator.normal(loc = 0.0, scale = self.sigma)
			self.wBar[0] = (Env.theta +)
			self.n[0] = 100
			self.popID = name
		else:
			TypeError("Bad Mode Selection")

class EvoEnv(object):
	"""
	Variables:
	name(str)		- counter for current generation
	theta(float)	- optimal value of z for environment instance
	envID(str)		- population string identifier
	Base Mode:
		- creates an instance of EvoPop that is designed to simulate
		one population
	"""
	def __init__(self, mode, name = "Env", tmax=100):
		self.theta = float()
		self.env_mode = str()
		self.name = str()
		if mode == "base":
			self.env_mode = "stable"
			self.theta = 0.0
			self.name = name
		else:
			RaiseError("Invalid Mode")

def main():
	sim = EcoSim("base")



	####### Below __init__ iteration scratch
	#	self._mode() = mode
	#	self._base_time = 100
	#	if mode is not "base":
	#		return self._set_mode()


	#def _get_mode(self):
	#	"""
	#	"""
	#	return self._mode()
	#def _set_mode(self, m):
		# self._mode = str(m) if m is not none else m
	#	self._mode = m
	#mode = property(_get_mode, _set_mode)
	#def clone(self, depth=1):
	#	if depth == 0:
	#		return copy.copy(self)
	#	elif depth == 1:
	#		return self.simulation_scoped_copy(self):
	#	elif depth == 2:
	#		return copy.deepcopy(self)
	#	else:
	#		TypeError("Cloning Depth not supported: {}".format(depth))
	## SET GLOBAL VARIABLES
