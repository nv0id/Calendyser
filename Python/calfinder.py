#!/usr/local/bin/python3

# Find path names of all .calendar folders


import glob
import os
import dateutil.parser   # For dealing with the YYYYMMDDTHHMMSS datetime format

def file_ext_search(path,ext):
    return glob.glob(path + '/**/*%s'%ext, recursive=True)

def to_date(datestring):
    if datestring=="Null":
        return
    return dateutil.parser.parse(datestring)

def sql_clean(string):
    string = str(string)
    b = "!@: %^<>.,/*()#-;±§£'|][{}+=~`\""
    string = string.replace(" ","_")
    string = string.replace("-","_")
    for char in b: string=string.replace(char,"")
    return "\'"+string+"\'"


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

class event:
    def __init__(self,path):

        self.eend=self.ename=self.elocation=self.ebegin=self.filename="Null"

        with open(path,'r') as f: # Search through .ics file and find metatata
            for line in f: # Searches line by line to save memory
                if 'DTEND' in line:
                    self.eend = sql_clean(line.split(':',1)[1])
                elif 'SUMMARY' in line:
                    self.ename = sql_clean(line[8:])
                elif 'LOCATION' in line:
                    self.elocation = sql_clean(line[9:])
                elif 'DTSTART' in line:
                    self.ebegin = sql_clean(line.split(':',1)[1])
                elif 'X-APPLE-SERVERFILENAME'in line:
                    self.filename = sql_clean(line[24:])

        if self.eend == "Null":
            self.duration = ("\'"+"AllDay"+"\'")
        else:
            self.duration = sql_clean(to_date(self.eend) - to_date(self.ebegin))


## Debug - Delete me later ##
#calendar = calfinder('/Users/nvoidmac/Documents/GitHub/Calendyser/Python/Data/Calendar.icbu')
#print(calendar.calnames)
def main():
    pass


if __name__ == "__main__":
    main()
