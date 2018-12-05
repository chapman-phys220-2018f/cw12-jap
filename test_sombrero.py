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
import sombrero as hat

def test_sombrero():
    assert hat.sombrero(-0.9, 0, np.arange(0, 2*np.pi*50, 0.001), 0.18)[-1] < -0.816
    assert hat.sombrero(-0.9, 0, np.arange(0, 2*np.pi*50, 0.001), 0.18)[-1] > -0.816