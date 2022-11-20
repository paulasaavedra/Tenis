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

path = 'C:/Users/paula/Documents/GitHub/Tenis/some_codes/'
df = pd.read_csv(path + 'atp_matches_2019.csv') 


# age difference between the winner and loser
df['age diff'] = abs(df['winner_age'] - df['loser_age'])


# Winners from a country in particular
country = 'ARG'
df_country = df.loc[ df['winner_ioc'] == country]

# Winners from a country and age < 25
country = 'ARG'
df_country_age = df.query('winner_ioc == "ARG" & winner_age < 25')

# Total minutes of matches won by ARG players
df[df['winner_ioc'] == 'ARG']['minutes'].sum()

# Describe
df[df['winner_name']=='Diego Schwartzman']['minutes'].describe()

#
df_ages_by_nation = df.groupby('winner_ioc')['winner_age'].mean()

