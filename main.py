import collections
import csv
import pandas as pd
import numpy as np
import re
from matplotlib import pyplot as plt

from collections import Counter

plt.style.use("fivethirtyeight")

dataset = pd.read_csv("Lotto7.csv", header=None)

df = pd.read_csv("Lotto7.csv")


drawn_1 = df[[("Winning Number 1")]]
count_numbers ={}

cols = list(df.columns.values)
Drawn_numbers2 = df.iloc[:, 2:11]


df["count"] = 1


df["Winning_1"] = (df.groupby(["Winning Number 1"]).count()["count"])
df["w2"] = dict(df.groupby(["2"]).count()["count"])
df["w3"] = dict(df.groupby(["3"]).count()["count"])
df["w4"] = dict(df.groupby(["4"]).count()["count"])
df["w5"] = dict(df.groupby(["5"]).count()["count"])
df["w6"] = dict(df.groupby(["6"]).count()["count"])
df["w7"] = dict(df.groupby(["7"]).count()["count"])
df["w8"] = dict(df.groupby(["Bonus Number 1"]).count()["count"])
df["w9"] = dict(df.groupby(["2.1"]).count()["count"])

df = df.fillna(0)



df["Lotto Number"] = range(532)
df["total"] = df["Winning_1"] + df["w2"] + df["w3"] + df["w4"] + df["w5"] + df["w6"] + df["w7"] + df["w8"] + df["w9"]
print(df.iloc[1:40, -10:])
total_balls_drawn = list(df["total"][:38])
ball_numbers = df["Lotto Number"][:38]
print(total_balls_drawn)

plt.bar(total_balls_drawn, ball_numbers, label="All Devs")
plt.legend()
plt.title("frequent balls drawn in Lotto 7")
plt.xlabel("Total balls drawn")
plt.ylabel("Ball numbers")


df.to_csv("Lotto_7_1.csv")



