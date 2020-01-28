#!/usr/local/bin/python3

## Breakdown and import event data into SQL database

import sqlite3
import calfinder

def sqlise(icbuIn,dbOut):
    '''
    Function takes the path to a Calendar.icbu file,
    finds every every event and puts it into a database.
    '''
    calendar = calfinder.calfinder(icbuIn)

    conn = sqlite3.connect(dbOut)
    c = conn.cursor()

    query_counter = 0

     # Cleaniing up the name to prevent SQL injection.
    c.execute("CREATE TABLE allevents (Calendar text, EventName text, Location text, AllDayEvent integer, TStart text, TFinish text, Duration text)") # Create a table for each Calendar found
    query_counter += 1
    for calname,path in calendar.calnames.items():
        calname = calfinder.sql_clean(calname)
        for eventpath in calfinder.file_ext_search(path,".ics"): # Searches for .ics files in that .calendar folder
            event = calfinder.event(eventpath) # Creates an instance of event.
            sql_cmd = "INSERT INTO allevents VALUES (%s, %s, %s, %s, %s, %s, %s)" %(calname, event.ename, event.elocation,event.allday, event.ebegin, event.eend, event.duration)
            query_counter += 1
            c.execute(sql_cmd) # Writes event data to DB


    conn.commit()
    conn.close()

    return ("Made "+str(query_counter)+" queries!")

sqlise('/Users/nvoidmac/Desktop/data.icbu','/Users/nvoidmac/Desktop/events.db')

def main():
    pass

if __name__ == "__main__":
    main()
