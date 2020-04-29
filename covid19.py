import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib as mpl
import numpy as np
import pandas as pd

# Reads the csv file, where the data is saved
covid = pd.read_csv('us.csv', parse_dates=['date'])
covid.set_index('date', inplace=True)

# Creates the graphics that shows the data
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.plot(covid['cases'], color='tab:green', label='Cases')
ax.plot(covid['deaths'], color='tab:red', label='Deaths')

#creates the legend
leg = ax.legend(loc='upper left', fancybox=True, shadow=True)
leg.get_frame().set_alpha(0.4)

#set ticks every week
ax.xaxis.set_major_locator(mdates.DayLocator(interval=3))
#set major ticks format
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d %B'))

ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))

#Sets x, y and title labels
ax.set_xlabel('Date')
ax.set_ylabel('Number of occurency', fontsize=12)
ax.set_title('Number of cases and deaths in US')

plt.xticks(rotation=45)

plt.show()
