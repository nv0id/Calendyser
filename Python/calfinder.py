#!/usr/local/bin/python3

# Find path names of all .calendar folders

def main():

    import glob
    import os

    def file_ext_search(path,ext):
        return glob.glob(path + '/**/*%s'%ext, recursive=True)

    class calfinder:
        def __init__(self,path): # Pass /path_to_.icbu
            self.cal_path = file_ext_search(path,".calendar") # Find paths for .calendar extension
            self.cal_names = []
            for i,path in enumerate(self.cal_path):
                try:
                    with open(path + '/Info.plist') as f:
                        x = f.read()
                    all_lines = x.split('\n')
                    for i,line in enumerate(all_lines):
                        if '>Title<' in line:
                            self.cal_names.append(all_lines[i+1][9:-9])
                except:
                    self.cal_names.append('Calendar %s'%(i+1))





        @staticmethod
        def findcal(path):
            pass

    calendar = calfinder('/Users/nvoidmac/Documents/GitHub/Calendyser/Python/Data/Calendar.icbu')
    print(calendar.cal_path)
    print(calendar.cal_names)

if __name__ == "__main__":
    main()
