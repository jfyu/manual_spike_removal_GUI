import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

class selection_Rectangle(object):
    def __init__(self):
        self.ax = plt.gca()
        self.rect = Rectangle((0,0), 1, 1,fc='none')
        self.x0 = None
        self.y0 = None
        self.x1 = None
        self.y1 = None
        self.pressed = False
        self.ax.add_patch(self.rect)
        self.ax.figure.canvas.mpl_connect('button_press_event', self.on_press)
        self.ax.figure.canvas.mpl_connect('button_release_event', self.on_release)
        self.ax.figure.canvas.mpl_connect('motion_notify_event', self.on_motion)

    def on_press(self, event):
        print 'press'
        self.pressed = True
        self.x0 = event.xdata
        self.y0 = event.ydata

    def on_release(self, event):
        self.pressed = False
        print 'release'
        self.x1 = event.xdata
        self.y1 = event.ydata
        self.rect.set_width(self.x1 - self.x0)
        self.rect.set_height(self.y1 - self.y0)
        self.rect.set_xy((self.x0, self.y0))
        self.ax.figure.canvas.draw()
    
    def on_motion(self,event):
        if self.pressed == False:
            return 
        self.x1 = event.xdata
        self.y1 = event.ydata
        self.rect.set_width(self.x1 - self.x0)
        self.rect.set_height(self.y1 - self.y0)
        self.rect.set_xy((self.x0, self.y0))
        self.ax.figure.canvas.draw()
x = np.linspace(0,3,100)
y = np.sin(x)
plt.plot(x,y)
a = selection_Rectangle()
plt.show()
