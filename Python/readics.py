
def main():

    # import icalendar # $pip install icalendar

    import dateutil.parser   # For dealing with the YYYYMMDDTHHMMSS datetime format

    ## Turns the datetime from ics file into something useable.
    def to_date(datestring):
        return dateutil.parser.parse(datestring)

    ## Class definition for events

    class event:
        def __init__(self,path):

            with open(path,'r') as f: # Search through .ics file and find metatata
                for line in f: # Searches line by line to save memory
                    if 'DTEND' in line:
                        self.eend = line[17:]
                    elif 'SUMMARY' in line:
                        self.ename = line[8:]
                    elif 'LOCATION' in line:
                        self.elocation = line[9:]
                    elif 'DTSTART' in line:
                        self.ebegin = line[19:]
                    elif 'X-APPLE-SERVERFILENAME'in line:
                        self.filename = line[24:]

            self.duration = (to_date(self.eend) - to_date(self.ebegin))



    event1 = event('/Users/nvoidmac/Documents/GitHub/Calendyser/Python/testevent.ics')

    print(event1.duration)
    print(event1.filename)





if __name__ == "__main__":
    main()
