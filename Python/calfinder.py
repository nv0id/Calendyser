#!/usr/local/bin/python3
# Find path names of all .calendar folders

## ---------- Imports ---------- ##

import glob
import os
import dateutil.parser

## ---------- Defining functions here ---------- ##

def file_ext_search(path,ext):
    return glob.glob(path + '/**/*%s'%ext, recursive=True)

def to_date(datestring):
    '''
    - Takes string as input
    - Tries to turn varable into datestring
    - Returns datestime string
    '''
    if datestring=="Null":
        return
    try: return dateutil.parser.parse(datestring)
    except: return "Null"

def sql_clean(string):
    '''
    - Takes any variable as input
    - Turns varable into string and makes it SQL-safe
    - Returns cleansed 'string'
    '''
    string = str(string)
    b = "!@: %^<>.,/*()#-;±§£'|][{}+=~`\""
    string = string.replace(" ","_")
    string = string.replace("-","_")
    for char in b: string=string.replace(char,"")
    return "\'"+string+"\'"

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

def main():
    pass


if __name__ == "__main__":
    main()
