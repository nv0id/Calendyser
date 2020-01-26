# Notes for Calendyser

### 26.01.2020 - Python ics.py library

Found this library by C4ptainCrunch. Could be useful at some point. It helps parse and write to ics data rather than us having to write it ourselves.

#### Install using:

```bash
$ pip install ics
```

#### Example:

```python
from ics import Calendar, Event
c = Calendar()
e = Event()
e.name = "My cool event"
e.begin = '2014-01-01 00:00:00'
c.events.add(e)
c.events
# [<Event 'My cool event' begin:2014-01-01 00:00:00 end:2014-01-01 00:00:01>]
with open('my.ics', 'w') as my_file:
    my_file.writelines(c)
# and it's done !

```

#### Links

https://pypi.org/project/ics/

http://github.com/C4ptainCrunch/ics.py

Note by Freddie - Updated 26.01.2020
