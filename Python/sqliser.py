#!/usr/local/bin/python3

## Breakdown and import event data into SQL database

import sqlite3
import readics
import calfinder

def main():
    calendar = calfinder.calfinder('/Users/nvoidmac/Documents/GitHub/Calendyser/Python/Data/Calendar.icbu')

    conn = sqlite3.connect('/Users/nvoidmac/Documents/GitHub/Calendyser/Python/events.db')
    c = conn.cursor()

    for calname,path in calendar.calnames.items():
        c.execute("CREATE TABLE "+calname+" (fileid text,name text,location text,start text,finish text)")


        for eventpath in file_ext_search(path,".ics"):
            event = readics.event(eventpath)
            c.execute("INSERT INTO "+calname+" VALUES (?, ?, ?, ?, ?)" (calname,event.filename, event.ename, event.elocation, event.ebegin, event.eend))


        conn.commit()

        conn.close()





if __name__ == "__main__":
    main()
