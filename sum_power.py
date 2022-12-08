# -*- coding: utf-8 -*-
"""
Created on Thu 8th Dec 2022
@author: Nikunj
"""
def sum_nth_root(a,b,c) :
    if c == 0:
        print("Please enter a valid no.")
    else :
        d = (a+b)^(1/c)
    return (d)
def nth_power(a,b,c) :
    if a==0 and b==0 and c==0 :
        print("Indeterminate form!")
    else :
        return ((a+b)^c)