#!/usr/local/bin/python3

## Breakdown and import event data into SQL database

import sqlite3
import readics
import calfinder

def main():
    calendar = calfinder.calfinder('Data/Calendar.icbu') # For testing - Put path to .icbu here!

    conn = sqlite3.connect('/Users/nvoidmac/Documents/GitHub/Calendyser/Python/events.db')
    c = conn.cursor()

    counter = 0

    for calname,path in calendar.calnames.items():
        calname = readics.sql_clean(calname)
        c.execute("CREATE TABLE "+calname+" (fileid text, name text, location text, start text, finish text,duration text)")

        for eventpath in calfinder.file_ext_search(path,".ics"):
            event = readics.event(eventpath)
            sql_cmd = "INSERT INTO "+calname+" VALUES (%s, %s, %s, %s, %s, %s)" %(event.filename, event.ename, event.elocation, event.ebegin, event.eend, event.duration)
            counter += 1
            c.execute(sql_cmd)


    conn.commit()

    conn.close()

    print ("Inserted "+str(counter)+" events into database!")



if __name__ == "__main__":
    main()
