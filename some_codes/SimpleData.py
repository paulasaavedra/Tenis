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
import matplotlib.pyplot as plt

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

# group by
df_ages_by_nation = df.groupby('winner_ioc')['winner_age'].mean()

# Winners who made the most aces in a match
aces_max = df.sort_values('w_ace',ascending=False).head(3)

# ARG number of won matches
arg_won_matches = df[df.winner_ioc == "ARG"].pivot_table(
    index=["winner_name"],
    values=["match_num"],
    aggfunc="count"
)
arg_won_matches.sort_values("match_num", ascending=False)

# pivot tables - option 1
arg_won_levels = df[df.winner_ioc == "ARG"].pivot_table(
    index=[
        "winner_name",
        "loser_name",
        "tourney_level",
        "minutes"
    ],
    values=["match_num"],
    aggfunc="count"
).reset_index()

# pivot tables - option 2
arg_won_time = df[df.winner_ioc == "ARG"].pivot_table(
    columns="tourney_level",
    index="winner_name",
    values="w_ace",
    aggfunc="sum"
)

plt.xticks(rotation=90 )
plt.plot(arg_won_time)
plt.show()
arg_won_time.plot()


arg_loser_name = df[df.winner_ioc == "ARG"].pivot_table(
    columns="round",
    index="winner_name",
    values="w_ace",
    aggfunc="sum"    
)
arg_loser_name.plot(figsize=(15,10))
