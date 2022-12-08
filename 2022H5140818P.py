# -*- coding: utf-8 -*-
"""
Created on Thu 8th Dec 2022
@author: Aditya
"""
def nth_root(a,b) :
    if b == 0:
        print("Please enter a valid no.")
    else :
        c= a^(1/b)
    return (c)
def nth_power(a,b) :
    if a==0 and b==0 :
        print("Indeterminate form!")
    else :
        return (a^b)

