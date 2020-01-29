#!/usr/local/bin/python3
## Breakdown and import event data into SQL database

import sqlite3
import calfinder
import datetime

def sqlise(icbuIn,dbOut):
    '''
    Function takes the path to a Calendar.icbu file,
    finds every every event and puts it into a database.
    '''
    ###
    try:
        open(dbOut, 'w').close()
    except:
        pass
    ###
    calendar = calfinder.calfinder(icbuIn)

    conn = sqlite3.connect(dbOut)
    c = conn.cursor()


     # Cleaniing up the name to prevent SQL injection.
    c.execute("""CREATE TABLE allevents (Calendar text,
    EventName TEXT NOT NULL,
                Location TEXT,
                AllDayEvent INTEGER NOT NULL,
                TStart timestamp,
                TFinish timestamp,
                Duration REAL)""") # Create a table for each Calendar found
    for calname,path in calendar.calnames.items():
        for eventpath in calfinder.file_ext_search(path,".ics"): # Searches for .ics files in that .calendar folder

            event = calfinder.event(eventpath) # Creates an instance of event.
            c.execute("INSERT INTO allevents VALUES (?, ?, ?, ?, ?, ?, ?)", (calname, event.ename, event.elocation,event.allday,event.ebegin,event.eend,str(event.duration)))


    conn.commit()
    conn.close()

sqlise('/Users/nvoidmac/Desktop/data.icbu','/Users/nvoidmac/Desktop/events.db')
#sqlise('C:\\Users\\gbowr\\Desktop\\data_example','events.db')


def main():
    pass

if __name__ == "__main__":
    main()
