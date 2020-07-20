#!/usr/bin/python3
import re
from csv import DictReader
from datetime import datetime
import numpy as np
from matplotlib.dates import date2num


class WeatherStatistics:

    def __init__(self):
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
        print(self.datetime_array,self.barpress_array)
        
def main():
    app = WeatherStatistics()

if __name__ == "__main__": main()
