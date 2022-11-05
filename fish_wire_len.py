#!/usr/bin/env python
# coding: utf-8


import matplotlib.pyplot as plt
import numpy as np

rot = lambda theta: np.array([[np.cos(-theta),-np.sin(-theta)], [np.sin(-theta), np.cos(-theta)]])
h = 1
r_base = 2
r = 1
offset = 1

base = [[0,h],[0,0],[-r_base,0], [r_base,0]]

verts = [[0,0],[0,h],[-r,h], [r,h]]

rot_verts = lambda t: np.dot(rot(t), np.array(verts).T).T + np.array([0,h])
rot_verts_for_plot = lambda p: zip(*p)

l = lambda t: np.linalg.norm(rot_verts(t)[2:4]-base[2:4],axis=1)

for p in base, rot_verts(0), rot_verts(np.pi/8):
    x, y = zip(*p)
    plt.plot(x, y)
plt.axis("equal")
plt.grid()
plt.show()


print(f"delta_l = {l(np.pi/8)-l(0)}")

