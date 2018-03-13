#!/usr/bin/env python

print("\nENVIRONMENT SETUP TEST\n")

#-------------------------------------------------
# MySQL
print("Connecting to the database and exercising MySQL...")

import pymysql as db

try:
    conn = db.connect(
        host='localhost',
        user='user',
        password='',
        db='db')
    c = conn.cursor()
    c.execute("SELECT VERSION()")
    data = c.fetchone()
    print("Database version : {}".format(data))
    conn.close()
except:
    print("Couldn't connect to DB")

print("\n\n")


#-------------------------------------------------
# Pandas
print("Exercising Pandas...")

import pandas as pd

df = pd.DataFrame.from_dict({'name':'bob', 'age':56}, orient='index')
print(df)

print("\n\n")


#-------------------------------------------------
# NumPy and SciPy
print("Exercising NumPy and SciPy")

import numpy as np
from scipy import special, optimize

f = lambda x: -special.jv(3, x)
sol = optimize.minimize(f, 1.0)
x = np.linspace(0, 10, 5000)
print(x)


print("\n\n")

#-------------------------------------------------
# Matplotlib
print("Exercising Matplotlib...")

import matplotlib
matplotlib.use('Agg') # use Agg backend (*before* pyplot) to fix issues when running in virtual environment
import matplotlib.pyplot as plt

p = plt.plot(x, special.jv(3, x), '-', sol.x, -sol.fun, 'o')
print(p)
# plt.show()

print("\n\n")

#-------------------------------------------------
# scikit-learn
print("Exercising scikit-learn...")

from sklearn import datasets

iris = datasets.load_iris()
print(iris.target_names)

print("\n\n")


#-------------------------------------------------
# TensorFlow
print("Exercising TensorFlow")

import tensorflow as tf

hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))

print("\n\n")
