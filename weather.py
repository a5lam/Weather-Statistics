#!/usr/bin/python3
import re
from csv import DictReader
from datetime import datetime
import numpy as np

from tkinter import *
from tkinter import ttk, messagebox

from matplotlib.dates import date2num, num2date
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import ( FigureCanvasTkAgg, NavigationToolbarTkAgg)


class WeatherStatistics:

    def __init__(self, master):
        #load data
        datetime_list, barpress_list = [], []
        datetime_re = re.compile(r'[\d]{2,4}') # regex to get datetime info

        for year in range (2012, 2016):
            fname = 'resources/Environmental_Data_Deep_Moor_{0}.txt'.format(year)
            print('Loading {0}'.format(fname))
            for row in DictReader(open(fname,'r'), delimiter ='\t'):
                barpress_list.append(float(row['Barometric_Press']))
                datetime_list.append(date2num(datetime(*list(map(int, datetime_re.findall(row['date       time    ']))))))

        self.datetime_array = np.array(datetime_list)
        self.barpress_array = np.array(barpress_list)
        # print(self.datetime_array,self.barpress_array)

        # build the gui
        master.title('Weather Stastistics')
        master.resuzable(True, True)
        master.state('zoomed')

        matplotlib.rc('font', size = 18)
        f = Figure()
        f.set_facecolor((0, 0, 0, 0))
        self.a = f.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(f, master)
        self.canvas.draw()
        toolbar_frame = ttk.Frame(master)  # needed to put navbar above plot
        toolbar = NavigationToolbar2TkAgg(self.canvas, toolbar_frame)
        toolbar.update()
        toolbar_frame.pack(side=TOP, fill=X, expand=0)
        self.canvas._tkcanvas.pack(fill=BOTH, expand=1)

        controls_frame = ttk.Frame(master)
        controls_frame.pack()

        ttk.Label(controls_frame, text='Start', font='Arial 18 bold').grid(row=0, column=0, pady=5)
        ttk.Label(controls_frame, text='(YYYY-MM-DD HH:MM:SS)', font='Courier 12').grid(row=1, column=0, padx=50,
                                                                                        sticky='s')
        self.start = StringVar()
        ttk.Entry(controls_frame, width=19, textvariable=self.start, font='Courier 12').grid(row=2, column=0,
                                                                                             sticky='n')
        self.start.set(str(num2date(self.datetime_array[0]))[0:19])

        ttk.Label(controls_frame, text='End', font='Arial 18 bold').grid(row=0, column=1, pady=5)
        ttk.Label(controls_frame, text='(YYYY-MM-DD HH:MM:SS)', font='Courier 12').grid(row=1, column=1, padx=50,
                                                                                        sticky='s')
        self.end = StringVar()
        ttk.Entry(controls_frame, width=19, textvariable=self.end, font='Courier 12').grid(row=2, column=1, sticky='n')
        self.end.set(str(num2date(self.datetime_array[-1]))[0:19])

        ttk.Button(controls_frame, text='Update', ).grid(row=3, column=0, columnspan=2, pady=10)
        ttk.Style().configure('TButton', font='Arial 18 bold')

def main():
    root = Tk()
    app = WeatherStatistics(root)
    root.mainloop()

if __name__ == "__main__": main()
