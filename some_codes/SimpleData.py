# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 09:48:01 2022

@author: Paula
"""

"""
atp_matches_2019.csv is a database of tennis ATP matches in 2019 by Jeff 
Sackmann (https://github.com/JeffSackmann).
"""


import pandas as pd

path = 'C:/Users/paula/documents/GitHub/Tenis/some_codes/'
df = pd.read_csv(path + 'atp_matches_2019.csv') 


# age difference between the winner and loser
df['age diff'] = abs(df['winner_age'] - df['loser_age'])


# Winners from a country in particular
country = 'ARG'
df_country = df.loc[ df['winner_ioc'] == country]