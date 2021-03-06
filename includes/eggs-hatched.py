import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt; plt.rcdefaults()

 
# data to plot
n_groups = 5
rainbow_trout = (80000, 120000, 90000, 40000, 140000)
brown_trout = (70000, 70000, 70000, 70000, 90000)
 
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.7
 
rects1 = plt.bar(index, rainbow_trout, bar_width,
alpha=opacity,
color='green',
label='Rainbow Trout')
 
rects2 = plt.bar(index + bar_width, brown_trout, bar_width,
alpha=opacity,
color='grey',
label='Brown Trout')
 
plt.xlabel('Years')
plt.ylabel('Number of eggs hatched')
plt.title('Number of eggs hatched from 2014 to 2018')
plt.xticks(index + bar_width, ('2014', '2015', '2016', '2017','2018'))
plt.legend()
 
plt.tight_layout()
plt.show()