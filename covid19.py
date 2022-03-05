from tkinter import Label, font
from tkinter.ttk import LabeledScale
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib as mpl
import numpy as np
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
fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(2,2,1)
ax1 = fig.add_subplot(2,2,2)

ax.plot(covid['cases'], color='tab:green', label='Cases')
ax1.plot(covid['deaths'], color='tab:red', label='Deaths')

#set ticks every week
ax.xaxis.set_major_locator(mdates.DayLocator(interval=50))
#set major ticks format
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d %B %y'))

ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))

#Sets x, y and title labels
ax.set_xlabel('Date', fontsize = 10, family='sans', weight='semibold')
ax.set_ylabel('Number of occurency', fontsize = 10, family='sans', weight='semibold')
ax.set_title('Number of cases in US')

# Rotates and right-aligns the x labels so they don't crowd each other.
for label in ax.get_xticklabels(which='major'):
    label.set(rotation=45, horizontalalignment='right')

ax1.set_title('Number of death in US')
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=50))
ax1.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d %B %y'))
ax1.set_xlabel('Date', fontsize = 10, family='sans', weight='semibold')
for label in ax1.get_xticklabels(which='major'):
    label.set(rotation=45, horizontalalignment='right')

ax.grid(True)
ax1.grid(True)

plt.show()
