#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 15:28:06 2018

@author: nataliecedeno
"""
#%%
#Student class that has the following attributes:

#name
#last name
#age
#master


class Student: 
    def __init__(self, name, last_name, age, master): 
        self.name = name
        self.last_name = last_name
        self.age = age
        self.master = master

natalie = Student("Natalie", "Cedeno", "26", "MDBI")

#%%