import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as tk
import pandas as pd

# Reads the csv file, where the data is saved
covid = pd.read_csv('us.csv', parse_dates=['date'])
covid.set_index('date', inplace=True)

# Data Screening
covid.shape
covid.columns

# Data Cleaning
sum(covid.groupby("date").cases.sum().diff() < 0)

plt.rcParams['font.family'] = 'sans'
plt.rcParams['font.weight'] = 'semibold'
plt.style.use('ggplot')

# Creates the graphics that shows the data
plt.figure(1)
ax = plt.subplot(211)
ax1 = plt.subplot(212)

ax.plot(covid['cases'], color='tab:green', label='Cases')
ax1.plot(covid['deaths'], color='tab:red', label='Deaths')

# Number of cases analysis
# set ticks every week
ax.xaxis.set_major_locator(mdates.DayLocator(interval=85))

# set major ticks format
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d %b %y'))
ax.yaxis.set_major_formatter(tk.StrMethodFormatter('{x:,.0f}'))

# Sets x, y and title labels
ax.set_xlabel('Date', fontsize=10, family='sans', weight='semibold')
ax.set_ylabel('Number of occurency', family='sans', weight='semibold')
ax.set_title('Cases in US')

# Rotates and right-aligns the x labels so they don't crowd each other.
for label in ax.get_xticklabels(which='major'):
    label.set(rotation=0, horizontalalignment='center')

# Number of death analysis
ax1.set_title('Death in US')
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=85))
ax1.yaxis.set_major_formatter(tk.StrMethodFormatter('{x:,.0f}'))
ax1.set_ylabel('Number of occurency', family='sans', weight='semibold')
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d %b %y'))
ax1.set_xlabel('Date', fontsize=10, family='sans', weight='semibold')
for label in ax1.get_xticklabels(which='major'):
    label.set(rotation=0, horizontalalignment='center')

ax.grid(True)
ax1.grid(True)

plt.show()
