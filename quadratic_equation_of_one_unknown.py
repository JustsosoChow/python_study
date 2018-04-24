#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def quadratic(a, b, c):
    if a!= 0:
        if (b*b-4*a*c) > 0 :
            temp = math.sqrt(b*b-4*a*c)
        else:
            return (print('error input'))
    else:
        return (print('The first number equal 0'))
    return((-b+temp)/(2*a),(-b-temp)/(2*a))

a,b,c = map(int,input('input the numbers:').split())
quadratic(a,b,c)