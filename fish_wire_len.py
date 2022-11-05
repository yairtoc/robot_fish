#!/usr/bin/env python
# coding: utf-8


import matplotlib.pyplot as plt
import numpy as np

#constants
h = 1
r_base = 2
r = 1
offset = 1
theta = np.pi/8

# vertices for drawing
base = [[0,h],[0,0],[-r_base,0], [r_base,0]]
top = [[0,0],[0,h],[-r,h], [r,h]]

# calculations
rot = lambda theta: np.array([[np.cos(-theta),-np.sin(-theta)], [np.sin(-theta), np.cos(-theta)]])
rot_top = lambda t: np.dot(rot(t), np.array(top).T).T + np.array([0,h])
l = lambda t: np.linalg.norm(rot_top(t)[2:4]-base[2:4],axis=1)

# drawing
plt.figure()
for p in base, rot_top(0), rot_top(theta):
    x, y = zip(*p)
    plt.plot(x, y)
plt.axis("equal")
plt.grid()
plt.show()
print(f"l_init =  {l(0)}")
print(f"l_rot =   {l(theta)}")
print(f"delta_l = {l(theta)-l(0)}")

