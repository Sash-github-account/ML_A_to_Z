# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 13:15:13 2019

@author: Sashwath
"""
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random

dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

#Implementation
N=10000 #no of samples/rounds
d= 10 #num of ads
ads_selected = []
num_of_reward_1 = [0] * d
num_of_reward_0 = [0] * d
sum_of_rewards = [0]*d
tot_rewards = 0

for n in range(0, N):
    add = 0
    max_random = 0
    for i in range(0,d):
        random_beta = random.betavariate(num_of_reward_1[i] +1, num_of_reward_0[i] +1)
        if random_beta > max_random:
            max_random = random_beta
            add = i
    ads_selected.append(add)
    reward = dataset.values[n, add]
    if(reward == 1):
        num_of_reward_1[add] = num_of_reward_1[add] + 1
    else:
        num_of_reward_0[add] = num_of_reward_0[add] + 1
    tot_rewards = tot_rewards + reward
    
    

# Visualising the results
plt.hist(ads_selected)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()