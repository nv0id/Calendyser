#!/usr/local/bin/python3

import dateutil.parser   # For dealing with the YYYYMMDDTHHMMSS datetime format

## Turns the datetime from ics file into something useable. ##
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

## Class definition for events. ##
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
#event1 = event('/Users/nvoidmac/Documents/GitHub/Calendyser/Python/testevent.ics')
#print(event1.duration)
#print(event1.filename)
def main():
    pass


if __name__ == "__main__":
    main()
