# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 19:29:18 2020

@author: littl
"""


data = []
count = 0
with open("reviews.txt", "r") as f: 
    for line in f: 
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))
l = len(data)
print("Total reviews: ", l)
print(data[0])
print("--------------")
print(data[1])
