//import necessary libraries
import numpy as np
import pandas as pds
import matplotlib.pyplot as plt
from matplotlib import pylab
import seaborn as sns

//for the sake of dark theme
sns.set_style("dark")
noShow = pds.read_csv('path to csv')

//sneak-peek
print(noShow.head())

//rename columns(if needed)
noShow.rename(columns = {'CurrName':'NewName',
                         }, inplace = True)
                         
//convert date times into datetime64 format
noShow.AppointmentRegistration = noShow.AppointmentRegistration.apply(np.datetime64)
noShow.AppointmentDate = noShow.AppointmentDate.apply(np.datetime64)

//calculate waiting time and round to number of days
daysToAppointment = noShow.AppointmentDate - noShow.AppointmentRegistration
daysToAppointment = daysToAppointment.apply(lambda x: x.total_seconds() / (3600 * 24))

//binary coding
noShow.Gender[noShow.Gender == 'male'] = 1
noShow.Gender[noShow.Gender == 'female'] = 0

//checking for outliers in Awaiting Time
sns.stripplot(data = noShow, y = 'AwaitingTime', jitter = True)
sns.plt.ylim(0, 500)
sns.plt.show()

//remove outliers
noShow = noShow[noShow.AwaitingTime < 350]

//check for negative ages
