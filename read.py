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
        
print("Finished reading. Total reviews:", len(data))

sum_len = 0
for d in data: 
    sum_len = sum_len + len(d)
print ("The average characters of the review (including space) are", sum_len/len(data), "characters.")