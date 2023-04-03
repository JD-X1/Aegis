#!usr/bin/python3
import os
import unittest
import copy
import sys
import pandas as pd
import numpy as np
import scipy as sp
import pathlib
path_root = pathlib.Path("../modules/").parents[0]
sys.path.append(str(path_root)+"/")
import modules.Evo as Evo

class TestEvoBase(unittest.TestCase):
	def test_initializationBase(self):
		"""
		Testing correct starting params for
		EvoPop initialization, and test
		correct error output for devolopment
		stage
		"""
		simu = Evo.EvoSim("base")
		self.assertEqual(simu.clock.timeType, "discrete")
		self.assertEqual(simu.clock.time, 0)
		self.assertEqual(simu.Env.name, "E1")
		self.assertEqual(simu.Env.theta, 0.5)
		self.assertEqual(simu.Env.env_mode, "stable")
		self.assertEqual(simu.Pop.gen, 0)
		self.assertEqual(simu.Pop.n, 100)
		self.assertEqual(simu.Pop.popID, "P1")
		self.assertTrue((simu.Pop.zBar == np.zeros([100,], dtype = float)).all())


if __name__ == '__main__':
    unittest.main()
