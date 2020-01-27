#!/usr/local/bin/python3

# Find path names of all .calendar folders


import glob
import os

def file_ext_search(path,ext):
    return glob.glob(path + '/**/*%s'%ext, recursive=True)

class calfinder:
    def __init__(self,path): # Pass /path_to_.icbu
        cal_path = file_ext_search(path,".calendar") # Find paths for .calendar extension

        # Getting calendar names
        cal_names = []
        for i,path in enumerate(cal_path):
            try:
                with open(path + '/Info.plist') as f:
                    x = f.read()
                all_lines = x.split('\n')
                for i,line in enumerate(all_lines):
                    if '>Title<' in line:
                        cal_names.append((all_lines[i+1][9:-9]).replace(" ",""))
            except:
                cal_names.append('Calendar%s'%(i+1))

        #Zip 'em up in a nice dictionary
        self.calnames = dict(zip(cal_names,cal_path))


## Debug - Delete me later ##
#calendar = calfinder('/Users/nvoidmac/Documents/GitHub/Calendyser/Python/Data/Calendar.icbu')
#print(calendar.calnames)
def main():
    pass


if __name__ == "__main__":
    main()
