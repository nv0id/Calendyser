#!/usr/local/bin/python3

## Breakdown and import event data into SQL database

import sqlite3
import calfinder

def sqlise(path):
    '''
    Function takes the path to a Calendar.icbu file,
    finds every every event and puts it into a database.
    '''
    calendar = calfinder.calfinder(path)

    conn = sqlite3.connect('/Users/nvoidmac/Documents/GitHub/Calendyser/Python/events.db')
    c = conn.cursor()

    counter = 0

    for calname,path in calendar.calnames.items():
        calname = calfinder.sql_clean(calname) # Cleaniing up the name to prevent SQL injection.
        c.execute("CREATE TABLE "+calname+" (fileid text, name text, location text, start text, finish text,duration text)") # Create a table for each Calendar found
        counter += 1

        for eventpath in calfinder.file_ext_search(path,".ics"): # Searches for .ics files
            event = calfinder.event(eventpath) # Creates an instance of event.
            sql_cmd = "INSERT INTO "+calname+" VALUES (%s, %s, %s, %s, %s, %s)" %(event.filename, event.ename, event.elocation, event.ebegin, event.eend, event.duration)
            counter += 1
            c.execute(sql_cmd) # Writes event data to DB


    conn.commit()
    conn.close()

    return ("Made "+str(counter)+" queries!")

def main():
    pass

if __name__ == "__main__":
    main()
