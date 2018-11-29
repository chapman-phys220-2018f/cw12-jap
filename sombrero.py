# Jessica Trawick
# trawick@chapman.edu
# Phys 220
# 2300326


import numpy as np

import sumpy as sp

import mathplotlib.pyplot as plt

def dxdt (x,y,t):
    "Only returns y"
    return y

def r4(x0,y0,F, v=.25,w=1):
    """Fourth order Runge Kutta Equation"""
    x[0]= x0
    y[0]=y0
    dt = .001
    t = np.arrange(0 (2*np.pi),dt)
    y = np.zeros_like(t)
    x = np.zeros_like(t)
    for i in range(0, len(t)):
        

def dydt (x,y,t,F,v,w):
    "creates an equation of duffing"
    dv = -x**3+x-v*y+F*(np.cos(w*t))
    return dv
