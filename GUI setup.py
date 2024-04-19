# a setup of the GUI layout using tkinter
#import the library
from tkinter import *

class Greenhouse(Frame):
    def __init__ (self, parent):
        Frame.__init__(self, parent, bg = "white")
        # initialization
        self.layout()

    # generalize width and height for all boxes
    WIDTH = 43
    HEIGHT = 7
    def layout(self):
        # create label for temperature display
        self.display = Label(self, text = "Current Greenhouse Temperature",
                             anchor = N, bg = "white",
                             height = self.HEIGHT, width = self.WIDTH,
                             font = ("Arial", 20))
        # create grid manager for label
        self.display.grid(row = 0, column = 0, columnspan = 3,\
                          sticky = E+W+N+S)
        
        # create label for Humidity display
        self.display = Label(self, text = "Current Greenhouse Humidity",
                             anchor = N, bg = "white",
                             height = self.HEIGHT, width = self.WIDTH,
                             font = ("Arial", 20))
        # create grid manager for label
        self.display.grid(row = 0, column = 3, columnspan = 3,\
                          sticky = E+W+N+S)
        
        # create label for ideal environment display
        self.display = Label(self, text = "Ideal Plant environment",
                             anchor = N, bg = "white",
                             height = self.HEIGHT, width = self.WIDTH,
                             font = ("Arial", 20))
        # create grid manager for label
        self.display.grid(row = 1, column = 0, columnspan = 3,\
                          sticky = E+W+N+S)
        
        # create label for soil moisuture display
        self.display = Label(self, text = "Current Soil Moisture",
                             anchor = N, bg = "white",
                             height = self.HEIGHT, width = self.WIDTH,
                             font = ("Arial", 20))
        # create grid manager for label
        self.display.grid(row = 1, column = 3, columnspan = 3,\
                          sticky = E+W+N+S)
        
        # create label for fan and mister status
        self.display = Label(self, text = "Status of Greenhouse Regulators",
                             anchor = N, bg = "white",
                             height = self.HEIGHT, width = self.WIDTH,
                             font = ("Arial", 20))
        # create grid manager for label
        self.display.grid(row = 2, column = 3, columnspan = 3,\
                          sticky = E+W+N+S)
        self.pack()

'''
        # button creation
        # create button to change the plant that is in the greenhouse
        img = PhotoImage(file = "add.gif")
        button = Button(self, bg = "white", image = img,\
                        command = lambda:self.process("+"))
        button.image = img
        button.grid(row = 3, column = 0, columnspan = 3,\
                    sticky = N+S+E+W)

        # pack the buttons
        self.pack(fill = BOTH, expand = 1)
'''


# some behavior
window = Tk() # creates a Tk object
window.title("The Smart Greenhouse")
g = Greenhouse (window)
window.mainloop()
