def execution_time():
    '''Time of execution of program'''
    import time

    intitalTime = time.time()                           # current time
    # function -> code from other functon
    
    finalTime = intitalTime - time.time()          # max - min
    print(finalTime)