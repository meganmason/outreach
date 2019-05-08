import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys

df = pd.read_csv('bogus_sno.txt', sep=",",header=56, names=["date", 'depth [cm]','SWE [mm]'])

# index_col='date'

sns.set_style('darkgrid')
sns.set_style("ticks")
sns.set_context('notebook') #[notebook, paper, talk, poster]


fig, a=plt.subplots(2,1)

a[0].plot(pd.to_datetime(df["date"]),df['depth [cm]'])
a[0].set_ylabel('Snow Depth [cm]')
a[0].set_title('Bogus Basin Snow depth')
# plt.legend()
a[0].grid(True)

a[1].plot(pd.to_datetime(df["date"]), df['SWE [mm]'].div(10),color="red")
# a[1].plot(pd.to_datetime(df["date"]),np.divide(df['SWE [mm]',10]),color="red")
a[1].set_xlabel('Year')
a[1].set_ylabel('SWE [cm]') #CONVERTED (for 7th grade comparison)

#examples
#a.set_ylim()
a[1].set_title('Bogus Basin Snow Water Equivalent (SWE)')
a[1].grid(True)
plt.show()



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#works - one plot
# sns.set_style('darkgrid')
# sns.set_style("ticks")
# sns.set_context('notebook') #[notebook, paper, talk, poster]
#
#
# f=plt.figure()
# a=plt.gca()
# a.plot(pd.to_datetime(df["date"]),df['SWE [mm]'])
# a.plot(pd.to_datetime(df["date"]),df['depth [cm]'])
# plt.xlabel('Year')
# plt.ylabel('Snow Depth [cm]')
# plt.title('Bogus Basin Snow Depth')
# plt.legend()
