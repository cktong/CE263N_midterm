# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

file = open('housing_midterm_trn.csv', 'rb')
data = np.genfromtxt(file, delimiter=',',skip_header=1)

print(data, data.shape)