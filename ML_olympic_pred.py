#first time when I was typing this code

import pandas as pd

df = teams = pd.read_csv("teams.csv")
teams
print(df)

teams = teams [["team", "country", "year", "athletes","age", "prev_medals", "medals"]]
teams

print(teams)

print(teams.corr(numeric_only=True)["medals"])

#Thursday 25 July 2024 12:45 pm

import seaborn as sns

sns.lmplot(x="athletes", y="medals", data=teams, fit_reg=True, ci=None )

sns.lmplot(x="age", y="medals", data=teams, fit_reg=True, ci=None)

from seaborn.matrix import plt


#Thursday August 1 2024 2:30pm

teams.plot.hist(y="medals")

plt.show()


#a bit data cleaning
#first finding them 

x = teams[teams.isnull().any(axis=1)]

print(x)




