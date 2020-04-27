import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Reads the csv file, where the data is saved
covid = pd.read_csv('us.csv', parse_dates=['date'])

# Creates the graphics that shows the data
fig = plt.figure()
ax = fig.add_subplot(2, 1, 1)

ax.plot(covid['date'], covid['cases'], color='tab:green', label='Cases')
ax.plot(covid['date'], covid['deaths'], color='tab:red', label='Deaths')

#creates the legend
leg = ax.legend(loc='upper left', fancybox=True, shadow=True)
leg.get_frame().set_alpha(0.4)

#Sets x, y and title labels
ax.set_xlabel('Date')
ax.set_ylabel('Number of occurency')
ax.set_title('Number of cases and deaths in US')

plt.show()
