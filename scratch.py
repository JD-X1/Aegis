#!usr/bin/python3

import sys
sys.path.append("./modules")
import modules.Evo as Evo

simu = Evo.EvoSim("base")
simu.time_step()
