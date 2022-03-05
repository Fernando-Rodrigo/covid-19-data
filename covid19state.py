import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib as mpl
import seaborn as sns
import numpy as np
import pandas as pd

# Reads the csv file, where the data is saved
covid = pd.read_csv('us-states.csv', parse_dates=['date'])
covid.set_index('date', inplace=True)

# Data Screening
covid.shape
covid.columns
covid.state.nunique()

# Data Cleaning
sum(covid.groupby("date").cases.sum().diff() < 0)

plt.rcParams['font.family'] = 'sans'
plt.rcParams['font.weight'] = 'semibold'
plt.style.use('ggplot')

# Data Analysis
worst20 = covid.groupby("state").cases.sum().sort_values().tail(20).index.tolist()
states = pd.DataFrame(covid[covid.state.isin(worst20)].groupby(["date", "state"]).cases.sum().reset_index())

# Creates the graphics that shows the data
fig = plt.figure(figsize=(4, 3))
ax = fig.add_subplot(1, 1, 1)

#set ticks every week
ax.xaxis.set_major_locator(mdates.DayLocator(interval=40))
#set major ticks format
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d %b %y'))

ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))

ax.set_title('Number of cases per state in US')
sns.lineplot(data = states, x="date", y="cases", hue = "state", palette = "muted")

ax.set_xlabel('Date', fontsize = 10, family='sans', weight='semibold')
ax.set_ylabel('Number of occurency', fontsize = 10, family='sans', weight='semibold')

# Rotates and right-aligns the x labels so they don't crowd each other.
for label in ax.get_xticklabels(which='major'):
    label.set(rotation=30, horizontalalignment='right')


ax.grid(True)

plt.show()
