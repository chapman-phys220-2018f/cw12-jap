#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Name: Alley Busick, Jessica Trawick, Paul
# Student ID: 2293544, 2300326
# Email: busick@chapman.edu, trawick@chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2018
# Assignment: CW12
###

import numpy as np
import numba as nb
import matplotlib.pyplot as plt

@nb.jit #decorator
def dxdt(x, y, t):
    """returns y"""
    return y

@nb.jit
def dydt(x, y, t, F, v, w):
    """motion equation or duffing oscillator"""
    dy = x - x**3 - v*y + F*(np.cos(w*t))
    return dy

@nb.jit
def rk4(x0, y0, F, v, w, t):
    """Fourth order Runge Kutta Equation"""
    x[0]= x0
    x = np.zeros(t)
    y[0]= y0
    y = np.zeros(t)
    dt = t[1] - t[0]
    # ??????? t = np.arrange(0 (2*np.pi),dt)
    for i in range(0, len(t)-1):
        x1 = dt*dxdt(x[i], y[i], t[i])
        y1 = dt*dydt(x[i], y[i], t[i], F, v, w)
        x2 = dt*dxdt(x[i] + x1/2, y[i] + y1/2, t[i] + dt/2)
        y2 = dt*dydt(x[i] + x1/2, y[i] + y1/2, t[i] + dt/2, F, v, w)
        x3 = dt*dxdt(x[i] + x2/2, y[i] + y2/2, t[i] + dt/2)
        y3 = dt*dydt(x[i] + x2/2, y[i] + y2/2, t[i] + dt/2, F, v, w)
        x4 = dt*dxdt(x[i] + x3/2, y[i] + y3/2, t[i] + dt/2)
        y4 = dt*dydt(x[i] + x3/2, y[i] + y3/2, t[i] + dt/2, F, v, w)
        
        x[i+1] = x[i] + ((x1 + 2)*(x2 + 2)*x3 + x4)/6
        y[i+1] = y[i] + ((y1 + 2)*(y2 + 2)*y3 + y4)/6
    
    
    
