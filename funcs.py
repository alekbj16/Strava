import numpy as np
from dateutil import parser

def convert_to_datetime(stravaTimes):
    """
    stravaTimes is a array on containg elements in string form "Month Day, Year, Clock", e.g.: Sep 29, 2020, 5:09:59 PM or May 11, 2021, 4:41:34 PM
    """
    rundates_datetime = []
    #runDates
    for run in stravaTimes:
        #print(run)
        date = run
        #date = ",".join(run.split(",",2)[:-1])
        dt = parser.parse(date)

        #print(type(dt))    
        rundates_datetime.append(dt)   
    return rundates_datetime 
        #".".join(a.split(".", 3)[:-1])



if __name__ == "__main__":
    print("Running funcs.py")
    values = np.array(['Sep 29, 2020, 5:09:59 PM', 'Oct 17, 2020, 7:38:41 AM',
       'Nov 5, 2020, 3:49:20 PM', 'Nov 15, 2020, 6:58:25 PM',
       'Nov 29, 2020, 7:27:00 PM', 'Dec 1, 2020, 6:37:39 PM',
       'Dec 26, 2020, 2:33:52 PM', 'Jan 5, 2021, 12:02:43 PM',
       'Feb 28, 2021, 1:19:55 PM', 'Mar 2, 2021, 5:06:22 PM',
       'Mar 8, 2021, 5:33:18 PM', 'Mar 15, 2021, 4:03:57 PM',
       'Mar 20, 2021, 12:19:00 PM', 'Apr 12, 2021, 4:25:08 PM',
       'Apr 16, 2021, 7:11:31 PM', 'Apr 17, 2021, 9:32:46 AM',
       'Apr 23, 2021, 6:25:54 PM', 'Apr 26, 2021, 4:55:28 PM',
       'Apr 28, 2021, 12:21:05 PM', 'May 11, 2021, 4:41:34 PM',
       'May 15, 2021, 5:20:52 PM'], dtype=object)
    convert_to_datetime(values)
