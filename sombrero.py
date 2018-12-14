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

@nb.jit
def duffing(t, a, F):
    """Motion equation or duffing oscillator - a is an array"""
    #v = 0.25
    #w = 1
    d = np.array([a[1], -0.25*a[1] + a[0] - a[0]**3 + F*np.cos(t)])
    return d #derivative of function

@nb.jit
def sombrero(F, x, y, N):
    """Fourth order Runge Kutta Equation"""
    step = 0.001
    t = np.arange(0, 2*np.pi*N, step)
    #different time values
    length = len(t)
    time = np.zeros((length+1, 2))
    time[0] = np.array([x, y])
    n = 1

    for n in range(length):
        k1 = step*(duffing(t[n], time[n], F))
        k2 = step*(duffing(t[n] + step/2, time[n] + (k1/2), F))
        k3 = step*(duffing(t[n] + step/2, time[n] + (k2/2), F))
        k4 = step*(duffing(t[n] + step, time[n] + k3, F))
        time[n+1] = time[n] + ((k1 + 2*k2 + 2*k3 + k4)/6)
    return np.array([time[:,0], time[:,1]])

def line(vals, F, title):
    plt.plot(vals[0], vals[1], color="m", label="Oscillation")
    plt.plot(title) #differentiate graphs for various values
    plt.legend()
    plt.show()

def scatter(vals, F, title):
    plt.scatter(vals[0], vals[1], color="m", label="Oscillation", s=2)
    plt.plot(title)
    plt.legend()
    plt.ylim((-3,3))
    plt.xlim((-3,3))
    plt.show()