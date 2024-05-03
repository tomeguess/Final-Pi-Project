# a setup of the GUI layout using tkinter
#import the library

from tkinter import *
import threading
import serial
from time import sleep

# Class used to Read Serial monitor values
class SerialReader:
    def __init__(self, port, baudrate):
        self.ser = serial.Serial(port, baudrate)
        self.temp = 0
        self.humidity = 0
        self.moisture = 0
        self.fanstatus = " "
        self.misterstatus = " "
        self.running = False

    
    def start_reading(self):
        self.running = True
        threading.Thread(target=self.read_data).start()

    def read_data(self):
        while self.running:
            line = self.ser.readline().decode().strip()
            values = line.split(",")
            if len(values) == 5:
                self.temp = float(values[0])
                self.humidity = float(values[1])
                self.moisture = int(values[2])
                self.fanstatus = str(values[3])
                self.misterstatus = str(values[4])

    def stop_reading(self):
        self.running = False


class Greenhouse(Frame):
    def __init__ (self, parent):
        Frame.__init__(self, parent, bg = "white")
        # initialization
        self.layout()
        self.parent =parent

    # generalize width, height, and color for all boxes
    WIDTH = 43
    HEIGHT = 7
    FILL_HEIGHT= 3
    COLOR = "snow2"
    FONT = "Georgia"
    def layout(self):
        # create label for temperature display
        self.tempdisplay = Label(self, text = "Current Greenhouse Temperature \n\n\n update",
                             anchor = N, bg = self.COLOR,
                             height = self.HEIGHT, width = self.WIDTH,
                             font = (self.FONT, 20))
        # create grid manager for label
        self.tempdisplay.grid(row = 0, column = 0, columnspan = 3,\
                          sticky = E+W+N+S)
        
        # create label for Humidity display
        self.humdisplay = Label(self, text = "Current Greenhouse Humidity \n\n\n update",
                             anchor = N, bg = self.COLOR,
                             height = self.HEIGHT, width = self.WIDTH,
                             font = (self.FONT, 20))
        # create grid manager for label
        self.humdisplay.grid(row = 0, column = 3, columnspan = 3,\
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
        self.moistdisplay = Label(self, text = "Current Soil Moisture \n\n\n update",
                             anchor = N, bg = self.COLOR,
                             height = self.HEIGHT, width = self.WIDTH,
                             font = (self.FONT, 20))
        # create grid manager for label
        self.moistdisplay.grid(row = 1, column = 3, columnspan = 3,\
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
        self.regulatordisplay = Label(self, text = "Fan: \n Mister: \n Soil Moisture:",
                             anchor = W, bg = self.COLOR,
                             height = self.FILL_HEIGHT, width = self.WIDTH,
                             font = (self.FONT, 20))
        # create grid manager for label
        self.regulatordisplay.grid(row = 2, column = 3, columnspan = 3,\
                          sticky = W)
        self.pack()

        # button creation
        # create button to change the plant that is in the greenhouse
        # img = PhotoImage(file = "change plant button.PNG")
        # button = Button(self, bg = "white", image = img)
        # button.image = img
        # button.grid(row = 2, column = 0, columnspan = 3,\
        #             sticky = N+S+E+W)

        # pack the buttons
        self.pack(fill = BOTH, expand = 1)

    def update_labels(self):
        if self.serial_reader:
            self.tempdisplay.config(text=f"Current Greenhouse Temperature \n\n\n{self.serial_reader.temp}")
            self.humdisplay.config(text=f"Current Greenhouse Humidity \n\n\n{self.serial_reader.humidity}")
            self.moistdisplay.config(text=f"Current Soil Moisture \n\n\n{self.serial_reader.moisture}")
            self.regulatordisplay.config(text = f"Fan:\t{self.serial_reader.fanstatus} \n Mister:\t{self.serial_reader.misterstatus} \n Soil Moisture:",)
        self.parent.after(1000, self.update_labels)

    def start_serial_reading(self):
        self.serial_reader = SerialReader('COM3', 9600)
        self.serial_reader.start_reading()
        self.update_labels()

    def stop_serial_reading(self):
        if self.serial_reader:
            self.serial_reader.stop_reading()
            self.parent.destroy()


# some behavior
if __name__ == "__main__":
    window = Tk()
    window.title("The Plant Palace")
    greenhouse = Greenhouse(window)
    greenhouse.start_serial_reading()
    window.protocol("WM_DELETE_WINDOW", greenhouse.stop_serial_reading)
    window.mainloop()
