import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

pd.set_option('display.float_format','{:.2f}'.format)

res = pd.read_excel('/Users/shubhan/Desktop/Projects/3rd_q_statistics/3rd_Q_statistics.xlsx')
pd_frame = pd.DataFrame(res)

# Create new column (Assist/Turnover Ratio)
pd_frame['Assist/Turnover Ratio'] = pd_frame['Assists Per Quarter'] / pd_frame['Turnovers Per Quarter']

# Top 15 Points Per Quarter
third_q_scoring = pd_frame.filter(items = ['Name', 'Points Per Quarter', 'Shooting %', '2 Point %', '3 Point %', 'Shooting % Total Game']).sort_values(by = "Points Per Quarter", ascending=False)[0:15]

# FG % 3rd Q vs FG % Entire Game
sns.scatterplot(data = third_q_scoring, y = "Name", x = "Shooting %", s = 50) 
sns.scatterplot(data = third_q_scoring, y = "Name", x = "Shooting % Total Game",  s = 50)
plt.legend(labels = ["3rd Q Shooting %", "Entire Game Shooting %"])
plt.show()

# Top 15 Assists Per Quarter
third_assists = pd_frame.filter(items = ['Name', 'Assists Per Quarter', 'Turnovers Per Quarter', 'Assist/Turnover Ratio', 'Assist/Turnover Ratio Game' ]).sort_values(by = "Assists Per Quarter", ascending=False)[0:15]

# Assist/Turn Ratio 3rd Q vs Assist/Turn Ratio Entire Game
sns.scatterplot(data = third_assists, y = "Name", x = "Assist/Turnover Ratio", s = 50)
sns.scatterplot(data = third_assists, y = "Name", x = "Assist/Turnover Ratio Game",  s = 50)
plt.legend(labels = ["Assist / Turnover Ratio 3rd Q", "Assist / Turnover Ratio Game"])
plt.show()

# Top 15 FG % (4.5 ppq & Total Points >= 150)
filtered_fg = pd_frame[(pd_frame['Points Per Quarter'] >= 4.5) & (pd_frame['Total Points'] >= 150)]
third_top_fg = filtered_fg.filter(items = ['Name', 'Shooting %', 'Shooting % Total Game', 'Points Per Quarter']).sort_values(by = "Shooting %", ascending = False)[0:15]

# FG % 3rd Q vs FG % Entire Game
sns.scatterplot(data = third_top_fg, y = "Name", x = "Shooting %", s = 50)
sns.scatterplot(data = third_top_fg, y = "Name", x = "Shooting % Total Game",  s = 50)
plt.legend(labels = ["Shooting % Per 3rd Q", "Shooting % Per Game"])
plt.show()

# Top 10 3 Point % (Total 3s attempted >= 175)
filtered_threes = pd_frame[(pd_frame['Total 3s'] >= 175)]
third_top_3fg = filtered_threes.filter(items = ['Name', '3 Point %', '3 % Entire Game', 'Points Per Quarter', 'Total 3s']).sort_values(by = "3 Point %", ascending = False)[0:10]

# 3 Point % 3rd Q vs 3 Point % Entire Game
sns.scatterplot(data = third_top_3fg, y = "Name", x = "3 Point %", s = 50)
sns.scatterplot(data = third_top_3fg, y = "Name", x = "3 % Entire Game",  s = 50)
plt.legend(labels = ["3 Point %", "3 Point % Entire Game"])
plt.show()
