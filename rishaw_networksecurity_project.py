# -*- coding: utf-8 -*-
"""Rishaw_NetworkSecurity_Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LU9tAyPzb4uBirKCxLwqT7DDRhbvCNZ3

1) Write a Program in Python to generate MD5 of string data.
"""

#MD5 Solution
import hashlib
X=input(" Enter string ")
print(hashlib.md5(X.encode('utf-8')).hexdigest())

import hashlib
print(hashlib.algorithms_available)

"""2) Write a Program in Python to generate hashes of string data using 3 algorithms from hashlib."""

#sha256
import hashlib
X=input(" Enter string ")
print(hashlib.sha256(X.encode('utf-8')).hexdigest())

#blake2b
import hashlib
X=input(" Enter string ")
print(hashlib.blake2b(X.encode('utf-8')).hexdigest())

#sha384
import hashlib
X=input(" Enter string ")
print(hashlib.sha384(X.encode('utf-8')).hexdigest())

"""3)Add salting and iterations to your hashes."""

#SALTING 
import hashlib

X = input(" Enter string ")
salt = "5gz"
password = X+salt
h = hashlib.md5(password.encode())
print(h.hexdigest())

#ITERATION
import hashlib
X=input(" Enter string ")
for i in range(0,9):
  h = hashlib.md5(X.encode())
  h.hexdigest()
print (h)

"""SUCESSFULLY COMPLETED ALL 3 TASKS! THANKYOU SIR!-------BY RISHAW PRAKASH"""