### Code to calculate the expected time lag between a photon and an axion of a given mass ###
### This is in order to test for the possibility of a time-delayed signal detection ###

import numpy as np
import math
from math import log10
from astropy import units as u
import decimal as d
from mpmath import *

#Define Precision
mp.dps=100
mp.prec=100

#Define Values Here
m_a = mpf(10e-3) #eV/c2
E_p = mpf(1e11) #eV
D = mpf(4e9) #pc

#Conversions
pc = mpf(3.086e16) #m
c = mpf(2.997e8) #m/s
eVc2 = mpf(1.782e-36) #kg
eV = mpf(1.609e-19) #J

#Calculation
gamma = E_p / m_a
beta=(1-(1/(gamma**2)))**0.5

t_p = D * pc / c #s
t_a = D * pc / (beta * c)
dt= t_a - t_p

print('Photon Time: ', t_p)
print('Axion Time: ', t_a)
#print('Axion Velocity: ', v_a)
print('Gamma: ', gamma)
print('Time Difference: ', dt)
#print('Time Difference: ', "{:e}".format(dt))
