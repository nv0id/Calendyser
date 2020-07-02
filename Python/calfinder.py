#!/usr/local/bin/python3
# Find path names of all .calendar folders

## ---------- Imports ---------- ##

import glob
import os
import datetime

#Git push test

## ---------- Defining functions here ---------- ##

def file_ext_search(path,ext):
    return glob.glob(path + '/**/*%s'%ext, recursive=True)

def to_date(datestring):
    if 'T' in datestring:
        datestring = datestring[0:14].split('T',1)
        return datetime.datetime.strptime(datestring[0]+datestring[1],'%Y%m%d%H%M%S')
    elif datestring=="Null":
        return
    elif 'T' not in datestring:
        return datetime.datetime.strptime(datestring,'%Y%m%d')
    else: datestring = "Null"

## ---------- Making Classes here ---------- ##

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

        with open(path,'r', encoding="utf8") as f: # Search through .ics file and find metatata
            for line in f: # Searches line by line to save memory
                if 'DTEND' in line:
                    self.eend = to_date(line.split(':',1)[1].rstrip())
                elif 'SUMMARY' in line:
                    self.ename = line[8:].rstrip().replace("\\n", ", ").replace("\\", "")
                elif 'LOCATION' in line:
                    self.elocation = line[9:].rstrip().replace("\\n", ", ").replace("\\", "")
                elif 'DTSTART' in line:
                    self.ebegin = to_date(line.split(':',1)[1].rstrip())
                ## Uncomment if you want file ID as well. ##
                #elif 'X-APPLE-SERVERFILENAME'in line:
                    #self.filename = line[24:])

        if self.eend == "Null":
            self.duration = "Null"
        else:
            self.duration = self.eend - self.ebegin
            self.duration = str((datetime.datetime.min + self.duration).time())
            self.duration = float(self.duration[0:2])+float(self.duration[3:5])/60+float(self.duration[7:9])/60/60

        try:
            if self.ebegin.hour == 0: self.allday = 1; self.duration = "Null"
            else: self.allday = 0 # Checks if all day event
        except:
            self.allday = "Null"


def main():
    pass


if __name__ == "__main__":
    main()
