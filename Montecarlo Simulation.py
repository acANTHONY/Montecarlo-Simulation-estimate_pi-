# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 20:41:08 2021

@author: USER
"""

import random

def estimate_pi(n):
    num_point_circle = 0
    num_point_total = 0
    for _ in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = x**2 + y**2
        if distance <= 1:
            num_point_circle += 1
        num_point_total += 1
    return 4 * num_point_circle/num_point_total

#100000000 = 3.14144628
# maybe = 10**9 = 3.1415