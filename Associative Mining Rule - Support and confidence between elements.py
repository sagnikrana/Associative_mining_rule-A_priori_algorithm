#!/usr/bin/env python
# coding: utf-8

# ### Associative mining rule

# Association rule mining is a technique to identify underlying relations between different items. Take an example of a Super Market where customers can buy variety of items. Usually, there is a pattern in what the customers buy. For instance, mothers with babies buy baby products such as milk and diapers. Damsels may buy makeup items whereas bachelors may buy beers and chips etc. In short, transactions involve a pattern. More profit can be generated if the relationship between the items purchased in different transactions can be identified.
# 
# For instance, if item A and B are bought together more frequently then several steps can be taken to increase the profit. For example:
# 
# A and B can be placed together so that when a customer buys one of the product he doesn't have to go far away to buy the other product.
# People who buy one of the products can be targeted through an advertisement campaign to buy the other.
# Collective discounts can be offered on these products if the customer buys both of them.
# Both A and B can be packaged together.
# The process of identifying an associations between products is called association rule mining. <br><br>
#   taken from "stackabuse.com"

# In[38]:


import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
from itertools import combinations


# In[60]:


data = pd.read_csv("data/items.csv", header = 'infer')

# Resolvig the column names into the numeric ones
for index,col in enumerate(list(data.columns)):
    data.rename(columns = {col:index}, inplace = True)

data.fillna("NA", inplace = True)
column_list = list(data.columns)
data


# #### Finding all the possible unique pairs:
# Assumption - duplicate items will not be repeated in the same row

# In[94]:


pairwise_info = {}
for rownum,row in data.iterrows():
    temp = []
    for col in column_list:
        if row[col] != 'NA':
            temp.append(row[col])
    pairs_per_row =  [sorted(item) for item in combinations(a, 2)]
    for pair_list in pairs_per_row:
        pair_name = ""
        for index,pair in enumerate(pair_list):
            if index == 0:
                pair_name = pair
            else:
                pair_name = pair_name + "+" + pair
        print(pair_name)
        print(pairwise_info)
        if pair_name not in pairwise_info:
            pairwise_info[pair_name] = [rownum]
        else:
            pairwise_info[pair_name] = pairwise_info[pair_name].append(rownum)


# In[92]:


pairwise_info


# ### Support <br>
# This is the percentage of orders that contains the item set. In the example above, there are 5 orders in total and {apple,egg} occurs in 3 of them, so:
# 
#              support{apple,egg} = 3/5 or 60%
# 
# The minimum support threshold required by apriori can be set based on knowledge of your domain. In this grocery dataset for example, since there could be thousands of distinct items and an order can contain only a small fraction of these items, setting the support threshold to 0.01% may be reasonable.
