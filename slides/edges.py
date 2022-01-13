#!/usr/bin/python
# -*- coding: UTF-8 -*-

import math

n = input("几边形?\n")
m = input("距原点距离？\n")
l = input("Slide 相对于平面偏转角度是？\n")

for i in range(n):

	xloc = round(m * math.cos(2 * math.pi * i / n), 2)
	yloc = round(m * math.sin(2 * math.pi * i / n), 2)

	xangel = round(l * math.cos(2 * math.pi * i / n), 2)
	yangel = round(l * math.sin(2 * math.pi * i / n), 2)

	angel = round((360.0 * i / n - 90) ,2)

	print(xloc, yloc, xangel, yangel, angel)