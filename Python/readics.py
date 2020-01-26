
def main():

    from datetime import datetime, date
    import icalendar # $pip install icalendar
    import pandas as pd


    class event:
        def __init__(self,e_name,e_location,e_begin,e_end):
            self.ename = e_name
            self.elocation = e_location
            self.ebegin = e_begin
            self.eend = e_end

        def duration(self):
            return (e_begin - e_end)

    a = pd.to_datetime('20161225T120000')
    b = pd.to_datetime('20161225T150000')
    event("MyEvent","Somewhere",a,b)

    print(event.duration(self))





if __name__ == "__main__":
    main()
