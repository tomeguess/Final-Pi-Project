# a setup of the GUI layout using tkinter
#import the library
from tkinter import *
from plant import *

class Greenhouse(Frame):
    def __init__ (self, parent):
        Frame.__init__(self, parent, bg = "white")
        # initialization
        self.layout()

    # generalize width, height, and color for all boxes
    WIDTH = 43
    HEIGHT = 7
    FILL_HEIGHT= 3
    COLOR = "snow2"
    FONT = "Georgia"
    def layout(self):
        # create label for temperature display
        self.display = Label(self, text = "Current Greenhouse Temperature \n\n\n update",
                             anchor = N, bg = self.COLOR,
                             height = self.HEIGHT, width = self.WIDTH,
                             font = (self.FONT, 20))
        # create grid manager for label
        self.display.grid(row = 0, column = 0, columnspan = 3,\
                          sticky = E+W+N+S)
        
        # create label for Humidity display
        self.display = Label(self, text = "Current Greenhouse Humidity \n\n\n update",
                             anchor = N, bg = self.COLOR,
                             height = self.HEIGHT, width = self.WIDTH,
                             font = (self.FONT, 20))
        # create grid manager for label
        self.display.grid(row = 0, column = 3, columnspan = 3,\
                          sticky = E+W+N+S)
        
        # create label for ideal environment display
        self.display = Label(self, text = "Ideal Plant environment",
                             anchor = N, bg = self.COLOR,
                             height = self.HEIGHT, width = self.WIDTH,
                             font = (self.FONT, 20))
        # create grid manager for label
        self.display.grid(row = 1, column = 0, columnspan = 3,\
                          sticky = E+W+N+S)
        # add rows to display ideal environment
        self.display = Label(self, text = f"Temperature: \n Humidity: \n Soil Moisture: ",
                             anchor = W, bg = self.COLOR,
                             height = self.FILL_HEIGHT, width = self.WIDTH,
                             font = (self.FONT, 20))
        # create grid manager for label
        self.display.grid(row = 1, column = 0, columnspan = 3,\
                          sticky = W)
        
        # create label for soil moisuture display
        self.display = Label(self, text = "Current Soil Moisture \n\n\n update",
                             anchor = N, bg = self.COLOR,
                             height = self.HEIGHT, width = self.WIDTH,
                             font = (self.FONT, 20))
        # create grid manager for label
        self.display.grid(row = 1, column = 3, columnspan = 3,\
                          sticky = E+W+N+S)
        
        # create label for fan and mister status
        self.display = Label(self, text = "Status of Greenhouse Regulators",
                             anchor = N, bg = self.COLOR,
                             height = self.HEIGHT, width = self.WIDTH,
                             font = (self.FONT, 20))
        # create grid manager for label
        self.display.grid(row = 2, column = 3, columnspan = 3,\
                          sticky = E+W+N+S)
        # add rows for fan, mister, and moisture display
        self.display = Label(self, text = "Fan: \n Mister: \n Soil Moisture:",
                             anchor = W, bg = self.COLOR,
                             height = self.FILL_HEIGHT, width = self.WIDTH,
                             font = (self.FONT, 20))
        # create grid manager for label
        self.display.grid(row = 2, column = 3, columnspan = 3,\
                          sticky = W)
        self.pack()

        # button creation
        # create button to change the plant that is in the greenhouse
        img = PhotoImage(file = "change plant button.PNG")
        button = Button(self, bg = "white", image = img)
        button.image = img
        button.grid(row = 2, column = 0, columnspan = 3,\
                    sticky = N+S+E+W)

        # pack the buttons
        self.pack(fill = BOTH, expand = 1)


# some behavior
window = Tk() # creates a Tk object
window.title("The Plant Palace")
g = Greenhouse (window)
window.mainloop()
