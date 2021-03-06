"""
Project: Big Data Competency Profile
By:      Raf M Rafaqut
About:   This Python (v2.7) Code Creates a Big Data Competency Profile Bar Chart as Described By
O'Neil &  Schutt p60 (2014) "Doing Data Science"
LinkedIn: https://www.linkedin.com/in/rafaqut
"""

import time
import pandas as pd
import os
import matplotlib.pyplot as plt

date = (time.strftime("%Y"))

#  Stats
name = 'Raf M Rafaqut'
bar_data_labels = ['Computer Science', 'Mathematics', 'Statistics', 'Machine Learning', 'Domain Expertise',
                   'Communication', 'Data Visualization']
bar_data = [70, 55, 80, 60, 50, 65, 60]# ratings from 0 to 100.
bar_data = pd.DataFrame(bar_data)

# output path
if not os.path.exists("%s_BD_Profile" % name):
    os.makedirs("%s_BD_Profile" % name)

# plot
bar_data.plot(kind='bar', color='pink', ylim=[0,100], legend=False,
              figsize=[15,7]).set_xticklabels(labels=bar_data_labels, rotation=0, fontsize=12)
plt.title("%s's Data Scientist Competency Profile %s" % (name, date), fontsize=22)
plt.xlabel('Competency', fontsize=15)
plt.ylabel("Competency Scale (0 to 100)", fontsize=15)
plt.savefig('BD_Profile.png')
