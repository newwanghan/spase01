#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plot

xmin = 0
xmax = 500
ymin = 1200
ymax = 2000

points1 = [
	(476, 1275),  # 109
	(446, 1289),
	(394, 1325),
	(332, 1379),
	(275, 1441),
	(226, 1505),
	(185, 1567),
	(149, 1624),
	(121, 1674),
	(97, 1717),
	(78, 1754),
	(63, 1785),
	(51, 1810),
	(41, 1830),
	(33, 1848),
	(27, 1862),
	(21, 1873),
	(17, 1882),
	(14, 1889),
	(11, 1895),
	(9, 1900),
	(8, 1904),
	(6, 1906),
	(4, 1909),
	(3, 1911),

]

fig = plot.figure(figsize=(6, 10))
# p = img.imread('./p1.png')
# fig.figimage(p)
plot.xlim(xmin, xmax)
plot.ylim(ymin, ymax)
ax = plot.gca()
ax.xaxis.set_ticks_position('top')
ax.invert_yaxis()
plot.grid()

# for x, y in points1:
# 	plot.plot([xmin, xmax], [y, y], color='b')
# 	plot.plot([x, x], [ymin, ymax], color='r')

plot.scatter([p[0] for p in points1], [p[1] for p in points1])
plot.plot([p[0] for p in points1], [p[1] for p in points1])

plot.show()
