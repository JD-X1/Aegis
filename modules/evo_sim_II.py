import numpy as np
from numpy.random import normal

def evo_sim(tmax, theta1, tau, h, sigmaE, sigmaG, beta, rmax, perror):

  # Initialize variables
  n = np.zeros(tmax); n[0] = 2
  x = np.zeros(tmax); x[0] = theta1 + normal(0, 0.0001)
  w = np.zeros(tmax-1)
  meanfit = np.zeros(tmax-1)

  # Process Error Distribution
  if perror == 0:
    pdist = [0, 0]
  else:
    pdist = normal(0, perror)

  def rfunc(mu, theta):
    r = rmax*tau*(np.exp(-((theta-mu)**2)/(2*((sigmaE**2 + sigmaG**2)+tau**2))))/(np.sqrt(tau**2+(sigmaE**2 + sigmaG**2)))
    return r

  for t in range(tmax-1):
    w[t] = (n[t]-1)/(n[t]-1+m)
    n[t+1] = ((rfunc(w[t]*x[t] + (1-w[t])*theta1, theta1) + normal(0, pdist))*(n[t]))*np.exp(-beta*(n[t]))
    meanfit[t] = (theta1 - w[t]*x[t] - (1-w[t])*theta1)/((sigmaE**2 + sigmaG**2) + tau**2)
    x[t+1] = w[t]*x[t] + (1-w[t])*theta1 + (h)*((sigmaG**2))*meanfit[t]

  return n, x, w
