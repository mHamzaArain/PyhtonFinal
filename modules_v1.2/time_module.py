from datetime import date
import datetime 
import time

# time.asctime()                                  -> Return formatted packed out of tuple
# time.localtime()                                -> Return local time construct  
# time.time()                                        -> Atomic time much lower than sec
# time.sleep(30)                                   -> Delay execution time in milli sec

# date.today()                                     -> Return date
# datetime.datetime.now()                   -> Return date & time not in good format

# ########Return date & time but not in well format
# dateTime = datetime.datetime.now()
# print(dateTime)  #  2019-09-20 21:29:02.415718

# ####################Return Time in milli sec
# time.sleep(30)
# print(time)

# ####################Return atomic clock time
# clockTick = time.time()
# print(clockTick)            # -> 1568996548.6967018


# ####################Return local time
# localTime = time.localtime()     # time.struct_time(tm_year=2019, tm_mon=9,
# print(t)                                       # tm_mday=20, tm_hour=21, tm_min=18,
                                                  # tm_sec=8, tm_wday=4,
                                                  # tm_yday=263, tm_isdst=0)

# #############################Return date
# today = date.today()
# print(today)        # 2019-09-20

# #############################Give Formated Date & Time
# localTime = time.asctime(time.localtime(time.time()))
# print(localTime)    # Fri Sep 20 21:13:16 2019


def execution_time():
    import time
    intitalTime = time.time()
    # function -> code from other functon
    finalTime = time.time() - intitalTime
    print(finalTime)