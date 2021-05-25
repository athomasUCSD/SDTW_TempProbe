import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import datetime

#becase always
style.use('fivethirtyeight')

#initialize the figs
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)


"""
animate function, reads the temp data file and sends to the plot
for updating
"""
def animate(i):
    graph_data = open('sensor_readings.txt','r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:

        entries = line.split(',')

        timestr = entries[0]
        time = datetime.datetime.strptime(
            timestr,
            format='%H:%M:%S %d/%m/%Y'
        )
        xs.append(float(time))
        ys.append(float(entries[2]))
    ax1.clear()
    ax1.plot(xs, ys)


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()