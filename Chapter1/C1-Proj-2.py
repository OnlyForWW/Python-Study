#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/31 19:52
# @Author  : JunyanWang
# @File    : C1-Proj-2.py
# @Description :

import math

def CalculateVolume():
    r = int(input("The radius of a sphere is: "))
    v = 4 / 3 * (r**3) * math.pi
    print(f"The volume of a shape is: {v}.")

if __name__ == "__main__":
    CalculateVolume()