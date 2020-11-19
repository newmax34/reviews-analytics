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
print ("The average characters of the review (including space):", sum_len/len(data), "(characters)")

new = []
for d in data: 
    if len(d) < 100:
        new.append(d)
print("How many reviews less than 100 characters?", len(new))

good = []
for d in data: 
    if "good" in d:
        good.append(d)
print("How many reviews mentioned 'good'?", len(good))

#文字記數
wc = {} #word_count
for d in data: 
    words = d.split()
    for word in words: 
        if word in wc:
            wc[word] += 1  
        else: 
            wc[word] = 1

for word in wc: 
    if wc[word] > 1000000:
        print(word, wc[word])

print(len(wc))

while True: 
    word = input("Enter the word you want to search:")
    if word == 'q':
        break
    if word in wc:
        print("The word:", "'", word, "'", "appears", wc[word], "time(s)")
    else: 
        print("This word never appears.")
        
print("Thank you for using this application.")














