    # -*- coding: utf-8 -*-
    """
    Created on Sun Sep 15 13:15:13 2019
    
    @author: Sashwath
    """
    # Importing the libraries
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd
    import math
    
    dataset = pd.read_csv('Ads_CTR_Optimisation.csv')
    
    #Implementation
    N=10000 #no of samples/rounds
    d= 10 #num of ads
    ads_selected = []
    num_of_sels = [0] * d
    sum_of_rewards = [0]*d
    tot_rewards = 0
    
    for n in range(0, N):
        add = 0
        max_UB = 0
        for i in range(0,d):
            if(num_of_sels[i] > 0):
                average_reward = sum_of_rewards [i] / num_of_sels[i]
                delta_i = math.sqrt(1.5*math.log(n+1)/num_of_sels[i])
                confidence_interval_UB = average_reward + delta_i
            else :
                confidence_interval_UB = 1e400
            if confidence_interval_UB > max_UB:
                max_UB = confidence_interval_UB
                add = i
        ads_selected.append(add)
        num_of_sels[add] = num_of_sels[add] + 1
        reward = dataset.values[n, add]
        sum_of_rewards[add] = sum_of_rewards[add] + reward
        tot_rewards = tot_rewards + reward
        
        

# Visualising the results
plt.hist(ads_selected)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()